import sensor, image, time, math, struct
from pyb import UART
import json

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
# 要检测颜色，所以使用彩色模式

sensor.set_framesize(sensor.QQVGA)
# 使用QQVGA降低画质提升运行速度

sensor.skip_frames(time=3000)
sensor.set_auto_whitebal(False)
# 颜色检测一定要关闭自动白平衡

clock = time.clock()
uart = UART(1, 115200)
uart.init(115200, bits=8, parity=None, stop=1)
# 上面是串口通信的部分

Red_threshold =[(13, 40, -2, 57, 11, 47),(29, 50, 13, 79, 15, 67),(33, 50, 16, 73, 2, 61)]
# 红色的LAB阈值

ROIS = {
    'down':(0,105,160,15),
    'middle':(0,52,160,15),
    'up':(0,0,160,15),
    'left':(0,0,15,120),
    'right':(145,0,15,120),
    'All':(0,0,160,120),
}
# 划分了上中下左右五个部分

class LineFlag(object):
    flag = 0
    cross_y = 0
    delta_x = 0
class EndFlag(object):
    endline_type = 0
    endline_y = 0
LineFlag=LineFlag()

'''
---变量解释---
Line.flag 路径标记
00	未检测到
01	直线
02	十/T路口
03	左转路口（顶部10像素以下）
04	右转路口（顶部10像素以下）
05	正在通过：十（无down块）
06	正在通过：左转T（无down块）
07	正在通过：右转T（无down块）
08	直线（无down块）

LineFlag.delta_x
0~160	红线底部在X轴的水平位置，左0右160，无down块时，返回middle块X轴水平位置

LineFlag.cross_y
0~120	红线路口交叉点的Y轴竖直位置，上0下120
'''
EndFlag=EndFlag()

# 红色实线部分函数
def find_blobs_in_rois(img):
    global ROIS
    roi_blobs_result = {}
    for roi_direct in ROIS.keys():
        roi_blobs_result[roi_direct] = {
            'cx': -1,
            'cy': -1,
            'blob_flag': False
        }
    for roi_direct, roi in ROIS.items():
        blobs=img.find_blobs(Red_threshold, roi=roi, merge=True, pixels_area=10)
        if len(blobs) == 0:
            continue
        largest_blob = max(blobs, key=lambda b: b.pixels())
        x,y,width,height = largest_blob[:4]
        if not(width >=3 and width <= 45 and height >= 3 and height <= 45):
            continue
        roi_blobs_result[roi_direct]['cx'] = largest_blob.cx()
        roi_blobs_result[roi_direct]['cy'] = largest_blob.cy()
        roi_blobs_result[roi_direct]['blob_flag'] = True


    if (roi_blobs_result['down']['blob_flag']):
        if (roi_blobs_result['left']['blob_flag']and roi_blobs_result['right']['blob_flag']):
            LineFlag.flag = 2 #十字路口或T路口
        elif (roi_blobs_result['left']['blob_flag']):
            LineFlag.flag = 3 # 左转路口
        elif (roi_blobs_result['right']['blob_flag']):
            LineFlag.flag = 4 # 右转路口
        elif (roi_blobs_result['middle']['blob_flag']):
            LineFlag.flag = 1 #直线
        else:
            LineFlag.flag = 0 # 未检测到
    else:
        if(roi_blobs_result['middle']['blob_flag']and roi_blobs_result['up']['blob_flag']):
            if (roi_blobs_result['left']['blob_flag']and roi_blobs_result['right']['blob_flag']):
                LineFlag.flag = 5 # 即将跨过十字路口
            elif (roi_blobs_result['left']['blob_flag']):
                LineFlag.flag = 6 # 即将跨过左拐T路口
            elif (roi_blobs_result['right']['blob_flag']):
                LineFlag.flag = 7 # 即将跨过右拐T路口
            else:
                LineFlag.flag = 8 # 直线（无down块）
        else:
            LineFlag.flag = 0

#	 特判
    # “本来是直线道路，但是太靠近左侧或者右侧，被识别成了左转或者右转”
    if (LineFlag.flag == 3 and roi_blobs_result['left']['cy']<10):
        LineFlag.flag = 1
    if (LineFlag.flag == 4 and roi_blobs_result['right']['cy']<10):
        LineFlag.flag = 1
    if (LineFlag.flag == 3 and roi_blobs_result['down']['cx']<30):
        LineFlag.flag = 1
    if (LineFlag.flag == 4 and roi_blobs_result['down']['cy']>130):
        LineFlag.flag = 1

    # 计算两个输出值，路口交叉点的纵坐标和直线时红线的偏移量
    LineFlag.cross_y = 0
    LineFlag.delta_x = 0

    if (LineFlag.flag == 1 or LineFlag.flag == 2 or LineFlag.flag == 3 or LineFlag.flag == 4) :
        LineFlag.delta_x = roi_blobs_result['down']['cx']
    elif (LineFlag.flag == 5 or LineFlag.flag == 6 or LineFlag.flag == 7 or LineFlag.flag == 8):
        LineFlag.delta_x = roi_blobs_result['middle']['cx']
    else:
        LineFlag.delta_x = 0

    if (LineFlag.flag == 2 or LineFlag.flag == 5):
        LineFlag.cross_y = (roi_blobs_result['left']['cy']+roi_blobs_result['right']['cy'])//2
    elif (LineFlag.flag == 3 or LineFlag.flag == 6):
        LineFlag.cross_y = roi_blobs_result['left']['cy']
    elif (LineFlag.flag == 4 or LineFlag.flag == 7):
        LineFlag.cross_y = roi_blobs_result['right']['cy']
    else:
        LineFlag.cross_y = 0

# 终点线黑色虚线
def find_endline(img):
    endbox_num = 0
    for r in img.find_rects(threshold = 10000):
        endbox_size = r.magnitude()
        endbox_w = r.w()
        endbox_h = r.h()
        k=1

        # 筛选黑色矩形大小
        if (endbox_size<24000*k*k and endbox_h<25*k and endbox_w<25*k) :
            endbox_num = endbox_num + 1;

    # 判断是否是终点线
    EndFlag.endline_type = 0
    if (endbox_num>2 and endbox_num<6):
        EndFlag.endline_type = 1 # 检测到一条终点线
    elif(endbox_num >=6 ):
        EndFlag.endline_type = 2 # 检测到两条终点线
    else:
        EndFlag.endline_type = 0 # 未检测到终点线

while(True):
    clock.tick()
    global img
    img = sensor.snapshot()

    img = img.replace(vflip=1,hmirror=1,transpose=0)
    # 倒装-做上下颠倒，看安装方式

    find_blobs_in_rois(img)
    # 巡线函数

    find_endline(img)
    # 找终点线函数

    FH = bytearray([0xc3,0xc3])
    uart.write(FH)
    # 发送帧头

    data = bytearray([LineFlag.flag, LineFlag.delta_x, LineFlag.cross_y, EndFlag.endline_type])
    uart.write(data)
    # 发送内容

    ED = bytearray([0xc4,0xc4])
    uart.write(ED)
    # 发送帧尾