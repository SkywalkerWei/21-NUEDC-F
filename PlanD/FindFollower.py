# Untitled - By: 22358 - 周日 11月 7 2021
import sensor, image, time, math             # 导入需要的库
from image import SEARCH_EX, SEARCH_DS
from pyb import LED
from pyb import UART
import json
import ustruct       # 串口通信
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QQVGA)             # 根据自己的摄像头参数进行调整
sensor.set_pixformat(sensor.GRAYSCALE)         # 灰色图片
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)                # 关闭白平衡
sensor.skip_frames(30)                         # 跳过前30帧使相机图像稳定下来

uart = UART(3,115200)                          # 串口设置
uart.init(115200, bits=8, parity=None, stop=1)

template1 = image.Image("/1.pgm")               # 前8个是数字模板，后面两个是十字和T字
template2 = image.Image("/2.pgm")
template3 = image.Image("/3.pgm")
template4 = image.Image("/4.pgm")
template5 = image.Image("/5.pgm")
template6 = image.Image("/6.pgm")
template7 = image.Image("/7.pgm")
template8 = image.Image("/8.pgm")
template9 = image.Image("/9.pgm")
template10 = image.Image("/10.pgm")
template10_1 = image.Image("/10_1.pgm")
#template10_2 = image.Image("/10_2.pgm")

def sending_data(uart_buf):                      # 串口通信格式的设定
    global uart;
    data = ustruct.pack("<bbhhb",            #格式为俩个字符俩个短整型(2字节)
                   0x2C,                       #帧头1
                   0x12,                       #帧头2
                   uart_buf,
                   0x5B)
    uart.write(data);                          #必须要传入一个字节数组
clock = time.clock()

low_threshold = (0, 66)         # 颜色阈值
RED_line = [(0, 64)]
ROIS = [                         # 感兴趣区域，
        (0, 100, 160, 40, 0.7),
        (0, 60, 160, 40, 0.3),
        (0, 20, 160, 40, 0.1)
       ]
#roi代表三个取样区域，（x,y,w,h,weight）,代表左上顶点（x,y）宽高分别为w和h的矩形，
#weight为当前矩形的权值。注意本例程采用的QQVGA图像大小为160x120，roi即把图像横分成三个矩形。
#三个矩形的阈值要根据实际情况进行调整，离机器人视野最近的矩形权值要最大，


weight_sum = 0               # 后面巡线需要使用的，权值和初始化
for r in ROIS:
    weight_sum += r[4]       # #计算权值和。遍历上面的三个矩形，r[4]即每个矩形的权值。



key = 0
t = 0
R = 0
text_contrast = ()
while(True):
    img = sensor.snapshot()
    img.binary([low_threshold], invert = 1)  # 根据像素是否在阈值列表 low_threshold中的阈值内，将图像中的所有像素设置为黑色
    img.draw_rectangle((50, 25, 60, 65), 0)   # 摄像头的感兴趣区域，在图像的中心一块，减少运算量；同时减少图像畸变带来的不准确性
    key = 0

     # 在此识别最开始给与的数字，因为模板匹配自身的一些机制，使得容易出错，所以设计了一个循环
    # 只有五次识别的数字相同，车辆才可以前进
    if key < 6:
        for i in range(5):       # img.find_template的第二个参数范围是（0—1），越接近1，拍摄图片相似度越高，元组参数使得在规定范围内检测
            r1 = img.find_template(template1, 0.65, (50, 25, 60, 65), step=4, search=SEARCH_EX)
            if r1:
                #img.draw_rectangle(r1, 0)
                R = 1
                text_contrast = r1
                #sending_data(R);
            r2 = img.find_template(template2, 0.55, (50, 25, 60, 65), step=4, search=SEARCH_EX)
            if r2:
                #img.draw_rectangle(r2, 0)
                R = 2
                text_contrast = r2
                #sending_data(1);
            r3 = img.find_template(template3, 0.72, (50, 25, 60, 65), step=4, search=SEARCH_EX)
            if r3:
                #img.draw_rectangle(r3, 0)
                R = 3
                text_contrast = r3
                #sending_data(1);
            r4 = img.find_template(template4, 0.55, (50, 25, 60, 65), step=4, search=SEARCH_EX)
            if r4:
                #img.draw_rectangle(r4, 0)
                R = 4
                text_contrast = r4
                #sending_data(1);
            r5 = img.find_template(template5, 0.72, (50, 25, 60, 65), step=4, search=SEARCH_EX)
            if r5:
                #img.draw_rectangle(r5, 0)
                R = 5
                text_contrast = r5
                #sending_data(1);
            r6 = img.find_template(template6, 0.70, (50, 25, 70, 65), step=4, search=SEARCH_EX)
            if r6:
                #img.draw_rectangle(r6, 0)
                R = 6
                text_contrast = r6
                #sending_data(1);
            r7 = img.find_template(template7, 0.55, (50, 25, 60, 65), step=4, search=SEARCH_EX)
            if r7:
                #img.draw_rectangle(r7, 0)
                R = 7
                text_contrast = r7
                #sending_data(1)
            r8 = img.find_template(template8, 0.65,  (50, 25, 60, 65),step=4, search=SEARCH_EX)
            if r8:
                #img.draw_rectangle(r8, 0)
                R = 8
                text_contrast = r8
                #sending_data(1);
            if t == 0:
                t = R
                continue
            elif t == R:       # 用来实现五次循环检测
                key = key + 1
                continue
            else:
                break
        if key == 5:
            img.draw_rectangle(text_contrast, 0)   # 将确定的检测物，框柱
            sending_data(1);                       # 车辆前进信号
        else:
            continue

        #print(t)    # 测试时用于确定检测到的数
        g = t
        break



while (True):
    clock.tick()
    img = sensor.snapshot()
    centroid_sum = 0
    img = sensor.snapshot()
    img.binary([low_threshold], invert = 1)


    for r in ROIS:                          # 实现十字路口和T字路口的识别，img.find_blobs（）导入红线数组RED_line，检测很灵敏准确，所以没有使用多次检测功能
        blobs = img.find_blobs(RED_line, roi=r[0:4], merge=True)      #找到视野中的线,merge=true,将找到的图像区域合并成一个
        r9 = img.find_template(template9, 0.65, step=4, search=SEARCH_EX)
        if r9:
            img.draw_rectangle(r9, 0)
            print("9")
            sending_data(2);
            key = 10
        r10 = img.find_template(template10, 0.65, step=4, search=SEARCH_EX)
        if r10:
            img.draw_rectangle(r10, 0)
            print("10")
            sending_data(2);
            key = 10

        if key > 9:   # 用来确认检测到了十字路口和T字路口，之后进入再次比对数字模式
            h = 0
            for i in range(4):

                                                                        #这里g和上面的R是相同的
                if g == 1:
                    r1 = img.find_template(template1, 0.55, step=4, search=SEARCH_EX)
                    if r1:
                        img.draw_rectangle(r1, 0)
                        print("100")                               # 测试时连电脑使用：img.draw_rectangle(r1, 0)；  print("100")
                        h = 100

                        if int(r1[0]+r1[2])/2  > 50:           # 通过获取检测图像的r1[0]检测图像的左上角横坐标；
                            print("右")                        # r1[2]图像的宽，通过判断是否超过图像的一半来确定左右转
                            sending_data(3);                   # 正常来说一半的分界线是80，但是因为摄像机的角度问题，使用50更为准确（摄像头偏右）
                        else:
                            print("左")
                            sending_data(4);                   # 向主控发送转弯信号
                if g == 2:
                    r2 = img.find_template(template2, 0.55, step=4, search=SEARCH_EX)
                    if r2:
                        img.draw_rectangle(r2, 0)
                        h = 200
                        print("200")

                        if int(r2[0] + r2[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if g == 3:
                    r3 = img.find_template(template3, 0.55, step=4, search=SEARCH_EX)
                    if r3:
                        img.draw_rectangle(r3, 0)
                        h = 300
                        print("300")
                        if int(r3[0]+r3[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if g == 4:
                    r4 = img.find_template(template4, 0.55, step=4, search=SEARCH_EX)
                    if r4:
                        img.draw_rectangle(r4, 0)
                        h = 400
                        print("400")
                        if int(r4[0]+r4[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if g == 5:
                    r5 = img.find_template(template5, 0.55, step=4, search=SEARCH_EX)
                    if r5:
                        img.draw_rectangle(r5, 0)
                        h = 500
                        print("500")
                        if int(r5[0]+r5[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if g == 6:
                    r6 = img.find_template(template6, 0.55, step=4, search=SEARCH_EX)
                    if r6:
                        img.draw_rectangle(r6, 0)
                        h = 600
                        print("600")
                        if int(r6[0]+r6[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if g == 7:
                    r7 = img.find_template(template7, 0.55, step=4, search=SEARCH_EX)
                    if r7:
                        img.draw_rectangle(r7, 0)
                        h = 700
                        print("700")
                        if int(r7[0]+r7[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if g == 8:
                    r8 = img.find_template(template8, 0.55, step=4, search=SEARCH_EX)
                    if r8:
                        img.draw_rectangle(r8, 0)
                        h = 800
                        print("800")
                        if int(r8[0]+r8[2])/2  > 50:
                            print("右")
                            sending_data(3);
                        else:
                            print("左")
                            sending_data(4);
                if h:
                    key = key - 1
                    continue
                else:
                    break

        if blobs:                                    # 用于实现巡线代码
            most_pixels = 0
            largest_blob = 0
            for i in range(len(blobs)):
            #目标区域找到的颜色块（线段块）可能不止一个，找到最大的一个，作为本区域内的目标直线
                if blobs[i].pixels() > most_pixels:
                    most_pixels = blobs[i].pixels()
                     #merged_blobs[i][4]是这个颜色块的像素总数，如果此颜色块像素总数大于
                     #most_pixels，则把本区域作为像素总数最大的颜色块。更新most_pixels和largest_blob
                    largest_blob = i
            img.draw_rectangle(blobs[largest_blob].rect())
            img.draw_rectangle((0,0,30, 30))
            #img.draw_rectangle((0,0,30, 30))
            #将此区域的像素数最大的颜色块画矩形和十字形标记出来

            img.draw_cross(blobs[largest_blob].cx(),
                           blobs[largest_blob].cy())
            centroid_sum += blobs[largest_blob].cx() * r[4]
            #计算centroid_sum，centroid_sum等于每个区域的最大颜色块的中心点的x坐标值乘本区域的权值

    center_pos = (centroid_sum / weight_sum)
       #中间公式

    deflection_angle = 0
    deflection_angle = -math.atan((center_pos-160)/120)
    #角度计算.80 60 分别为图像宽和高的一半，图像大小为QQVGA 160x120.
    #注意计算得到的是弧度值

    deflection_angle = math.degrees(deflection_angle)
    #将计算结果的弧度值转化为角度值

    A=deflection_angle
    uart_buf =int (A)+66
    print("Turn Angle: %d" % uart_buf)     #输出时强制转换类型为int
    sending_data(uart_buf);   #这个函数可以输出int型

