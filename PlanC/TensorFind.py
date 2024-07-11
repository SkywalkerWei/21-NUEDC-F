import sensor, image, time, os, tf,math
from pyb import UART
 
sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((320, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.
threshold_index = 0 # 0 for red, 1 for green, 2 for blue
 
# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green/blue things. You may wish to tune them...
thresholds = [(70, 4, 18, 127, -125, 127), # generic_red_thresholds
              (30, 100, -64, -8, -32, 32), # generic_green_thresholds
              (0, 30, 0, 64, -128, 0)] # generic_blue_thresholds
 
uart = UART(3, 115200)
 
net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]
net1 = "trained1.tflite"
labels1 = [line.rstrip('\n') for line in open("labels1.txt")]
crosstime=0
clock = time.clock()
aa=[0,0,0,0,0,0]
num=10
roi=(0,0,0,0)
flag=10#4识别数字 5巡线     6匹配数字  1继续寻找 0找到数字
direct=0        #第一个数据判断左右 0直行 1左拐 2右拐
while(True):
    clock.tick()
    size = uart.any();
    if size != 0:
        command = " "
        command = uart.read()
        flag = len(str(command))
        size = 0
        print(flag)
 
    while(flag==4):
        img = sensor.snapshot().lens_corr(1.8)
        if 1:
    # default settings just do one detection... change them to search the image...
            for obj in tf.classify(net1, img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
                img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
                predictions_list = list(zip(labels1, obj.output()))
 
                for i in range(len(predictions_list)):
                    if  predictions_list[i][1]>0.95:
                        num=i+1
                        output_str="[%3.d,%3.d]" % (num,7)
                        uart.write(output_str)
                        print(output_str)
                        flag=5
    if(flag==5):
        sensor.set_pixformat(sensor.RGB565)
        img = sensor.snapshot().lens_corr(1.8)
        found=0
        for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=200, area_threshold=200, merge=True):
        # These values depend on the blob not being circular - otherwise they will be shaky.
            if blob.elongation() > 0.5:
                img.draw_edges(blob.min_corners(), color=(255,0,0))
                img.draw_line(blob.major_axis_line(), color=(0,255,0))
                img.draw_line(blob.minor_axis_line(), color=(0,0,255))
        # These values are stable all the time.
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
        # Note - the blob rotation is unique to 0-180 only.
            img.draw_keypoints([(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20)
            found=1         #找到红线
            if blob.w()<250:
                output_str="[%3.d,%3.d]" % (blob.cx(),1)
            else:
                output_str="[%3.d,%3.d]" % (0,4)
        #print(blob.cx(),blob.w(),blob.rotation_deg())
        if found==0:
            output_str="[%3.d,%3.d]" % (0,6)
 
        uart.write(output_str)
        print(output_str)
 
    if(flag==6):
        sensor.set_pixformat(sensor.GRAYSCALE)
        img = sensor.snapshot().lens_corr(1.8)
        img1=img
        found=0
        output_str="[%3.d,%3.d]" % (0,5)
    # 下面的`threshold`应设置为足够高的值，以滤除在图像中检测到的具有
    # 低边缘幅度的噪声矩形。最适用与背景形成鲜明对比的矩形。
    #寻找第一个数字
        for r in img.find_rects(threshold = 10000):
            img.draw_rectangle(r.rect(), color = (255, 0, 0))
            for p in r.corners(): img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
            #print(r1.x(),r1.y(),r1.w(),r1.h())
            roi=[r.x(),r.y(),r.w(),r.h()]
            img1=img.copy(1,1,roi,True)
 
            for obj1 in tf.classify(net, img1, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
                img1.draw_rectangle(obj1.rect())
                # This combines the labels and confidence values into a list of tuples
                predictions_list = list(zip(labels, obj1.output()))
                if  predictions_list[num-1][1]>0.6:
                    found=1
                    print(num)
                    if  r.x()+r.w()/2<140:  #####左拐
                        output_str="[%3.d,%3.d]" % (1,5)
                    else:
                        output_str="[%3.d,%3.d]" % (2,5)
 
            uart.write(output_str)
            print(output_str)