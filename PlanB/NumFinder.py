import sensor, image, time, os, tf
from pyb import UART
import json
    
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.VGA)
sensor.skip_frames(time=2000)
    
net = "trainedv13.tflite"
    
# 透视校正用的四个点
TARGET_POINTS = [(143,210),(495,214),(640,480),(0,480)]
                     
# 识别数字的五个区域
ROI0 = (210,170,170,170)
ROI1 = (20,0,170,170)
ROI2 = (150,0,170,170)
ROI3 = (285,0,170,170)
ROI4 = (430,0,170,170)
    
# 反相后红色阈值
xred_threshold = (51, 84, -31, -3, -26, -2)
    
# 各区域识别数字准确度门槛，随倾斜度下降
keyline_0 = 0.7
keyline_1 = 0.6
keyline_2 = 0.65
keyline_3 = 0.65
keyline_4 = 0.6

ans_num = 0
   
clock = time.clock()
  
uart = UART(3, 115200)
uart.init(115200, bits=8, parity=None, stop=1)
    
while(True):
    clock.tick()
        
    img = sensor.snapshot().lens_corr(strength = 1.7, zoom = 0.55)
    img = img.replace(vflip=1,hmirror=1,transpose=0)
    img = img.rotation_corr(corners = TARGET_POINTS)
    img = img.negate()
    img = img.binary([xred_threshold], invert=False, zero=True)
    img = img.negate()
    
    # M
    for obj in tf.classify(net, img, roi=ROI0, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        out = obj.output()
        max_idx = out.index(max(out))
        if max(out)>keyline_0:
            ans_0 = max_idx + 1
        else:
            ans_0 = 0
        
    # LL
    for obj in tf.classify(net, img, roi=ROI1, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        out = obj.output()
        max_idx = out.index(max(out))
        if max(out)>keyline_1:
            ans_1 = max_idx + 1
        else:
            ans_1 = 0
    
    # LR
    for obj in tf.classify(net, img, roi=ROI2, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        out = obj.output()
        max_idx = out.index(max(out))
    
        if max(out)>keyline_2:
            ans_2 = max_idx + 1
        else:
            ans_2 = 0
    
    # RL
    for obj in tf.classify(net, img, roi=ROI3, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        out = obj.output()
        max_idx = out.index(max(out))
        if max(out)>keyline_3:
            ans_3 = max_idx + 1
        else:
            ans_3 = 0
    
    # RR
    for obj in tf.classify(net, img, roi=ROI4, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        out = obj.output()
        max_idx = out.index(max(out))
        if max(out)>keyline_4:
            ans_4 = max_idx + 1
        else:
            ans_4 = 0
    
    # 串口通信
    FH = bytearray([0xc3,0xc3])
    uart.write(FH)
    data = bytearray([ans_1, ans_2, ans_3, ans_4, ans_0])
    uart.write(data)
    ED = bytearray([0xc4,0xc4])
    art.write(ED)