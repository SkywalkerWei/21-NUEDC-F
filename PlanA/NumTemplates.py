import time, image,sensor,math,pyb
from image import SEARCH_EX, SEARCH_DS
from pyb import Pin, Timer,LED
uart = pyb.UART(3, 115200, timeout_char = 1000) 
sensor.reset()
 
sensor.set_contrast(1)#设置对比度
sensor.set_gainceiling(16)#设置增益上限
sensor.set_framesize(sensor.QQVGA)#设置图像分辨率为 QQVGA
sensor.set_pixformat(sensor.GRAYSCALE)#设置图像格式为灰度
#sensor.set_windowing(0, 0, 160, 160)#设置窗口大小,后面ROI设置也会以这个为新的基准
 
template01 = image.Image("/1.pgm")
template02 = image.Image("/2.pgm")
template03 = image.Image("/3.pgm")
template04 = image.Image("/4fly.pgm")
template05 = image.Image("/5.pgm")
template06 = image.Image("/6.pgm")
template07 = image.Image("/7.pgm")
template08 = image.Image("/8fly.pgm")

template3L = image.Image("/3L.pgm")
template3LL = image.Image("/3LL.pgm")
template3R = image.Image("/3R.pgm")
template3RR = image.Image("/3RR.pgm")
 
template4L = image.Image("/4L.pgm")
template4LL = image.Image("/4LL.pgm")
template4R = image.Image("/4R.pgm")
template4RR = image.Image("/4RR.pgm")
 
template5L = image.Image("/5L.pgm")
template5LL = image.Image("/5LL.pgm")
template5R = image.Image("/5R.pgm")
template5RR = image.Image("/5RR.pgm")
 
template6L = image.Image("/6L.pgm")
template6LL = image.Image("/6LL.pgm")
template6R = image.Image("/6R.pgm")
template6RR = image.Image("/6RR.pgm")
 
template7L = image.Image("/7L.pgm")
template7LL = image.Image("/7LL.pgm")
template7R = image.Image("/7R.pgm")
template7RR = image.Image("/7RR.pgm")
 
template8L = image.Image("/8L.pgm")
template8LL = image.Image("/8LL.pgm")
template8R = image.Image("/8R.pgm")
template8RR = image.Image("/8RR.pgm")
 
# 1.轮询1~8，直至识别到。  2.根据f103给的值，单纯识别那个数
Find_Task = 1#第几次匹配
TargetRoom = 0#需要到达的药房
find_flag = 0 #只声明，未使用

def FirstFindTemplate(template):
    Area = (50,38,70,53)
    R = img.find_template(template, 0.6, step=1,roi=Area, search=SEARCH_EX)#参数：1.检测的目标；2.精确度，越高越准；3.检测范围；4.跳过像素数量；5.算法，ex更精确，ds更慢
    img.draw_rectangle(Area, color=(255,255,255))
    return R

def FirstFindedNum(R, Finded_Num): #第一个参数是模板匹配的对象，第二个是它所代表的数字
   global Find_Task
   global find_flag
   global TargetRoom
   img.draw_rectangle(R, color=(225, 0, 0))
 
   #中值是80的，但返回值是框边缘，所以减去15  小于65是在左边，大于65是在右边
   find_flag = 1
   Num = Finded_Num
   print("Room：", Num)
   TargetRoom = Num
   Find_Task=2
 
   if Num == 1:
       uart.write("1")
 
   uart.write("start")
   print("start")

def FindTemplate(template):
    Area = (0, 30, 160, 50)
    R = img.find_template(template, 0.8, step=1, roi=Area, search=SEARCH_EX)
    img.draw_rectangle(Area, color=(255, 255, 255))
    return R
 
def FindedNum(R,Finded_Num):#第一个参数是模板匹配的对象，第二个是它所代表的数字
    global Find_Task
    global find_flag
    LoR = 0
    img.draw_rectangle(R, color=(225, 0, 0))
 
    #中值是80的，但返回值是框边缘，所以减去15  小于65是在左边，大于65是在右边
    if R[0] >= 65:
        LoR = 2
    elif 0< R[0] <65:
        LoR = 1
    find_flag = 1
    Num = Finded_Num
    print("识别到的数字是：", Num, "此数字所在方位：", LoR) #打印模板名字
    if LoR == 1:
        uart.write("Left")
        print("Left")
    elif LoR == 2:
        uart.write("Right")
        print("Right")
 
 
#=======================================主循环
clock = time.clock()
time.sleep(1)
while (True):
    clock.tick()
    img = sensor.snapshot()
 
    if Find_Task == 1:
        r01 = FirstFindTemplate(template01)
        r02 = FirstFindTemplate(template02)
        r03 = FirstFindTemplate(template03)
        r04 = FirstFindTemplate(template04)
        r05 = FirstFindTemplate(template05)
        r06 = FirstFindTemplate(template06)
        r07 = FirstFindTemplate(template07)
        r08 = FirstFindTemplate(template08)
 
        if r01:
             FirstFindedNum(r01,1)
        elif r02:
             FirstFindedNum(r02,2)
        elif r03:
             FirstFindedNum(r03,3)
        elif r04:
             FirstFindedNum(r04,4)
        elif r05:
             FirstFindedNum(r05,5)
        elif r06:
             FirstFindedNum(r06,6)
        elif r07:
             FirstFindedNum(r07,7)
        elif r08:
             FirstFindedNum(r08,8)
 
    elif Find_Task == 2: 
        if TargetRoom == 3:
            #进行模板匹配  //这里每个数字至少给3个模板， 但给五六个其实也行
            r3 = FindTemplate(template03)
            r3L = FindTemplate(template3L)
            r3LL = FindTemplate(template3LL)
            r3R = FindTemplate(template3R)
            r3RR = FindTemplate(template3RR)

            if r3L:
                FindedNum(r3L, 3)
            elif r3LL:
                FindedNum(r3LL, 3)
            elif r3R:
                FindedNum(r3R, 3)
            elif r3RR:
                FindedNum(r3RR, 3)
            elif r3:
                FindedNum(r3, 3)
 
        elif TargetRoom == 4:
            r4 = FindTemplate(template04)
            r4L = FindTemplate(template4L)
            r4LL = FindTemplate(template4LL)
            r4R = FindTemplate(template4R)
            r4RR = FindTemplate(template4RR)
 
            if r4L:
                FindedNum(r4L, 4)
            elif r4LL:
                FindedNum(r4LL, 4)
            elif r4R:
                FindedNum(r4R, 4)
            elif r4RR:
                FindedNum(r4RR, 4)
            elif r4:
                FindedNum(r4, 4)
 
        elif TargetRoom == 5:
            r5 = FindTemplate(template05)
            r5L = FindTemplate(template5L)
            r5LL = FindTemplate(template5LL)
            r5R = FindTemplate(template5R)
            r5RR = FindTemplate(template5RR)
 
            if r5L:
                FindedNum(r5L, 5)
            elif r5LL:
                FindedNum(r5LL, 5)
            elif r5R:
                FindedNum(r5R, 5)
            elif r5RR:
                FindedNum(r5RR, 5)
            elif r5:
                FindedNum(r5, 5)
 
        elif TargetRoom == 6:
            r6 = FindTemplate(template06)
            r6L = FindTemplate(template6L)
            r6LL = FindTemplate(template6LL)
            r6R = FindTemplate(template6R)
            r6RR = FindTemplate(template6RR)
 
            if r6L:
                FindedNum(r6L, 6)
            elif r6LL:
                FindedNum(r6LL, 6)
            elif r6R:
                FindedNum(r6R, 6)
            elif r6RR:
                FindedNum(r6RR, 6)
            elif r6:
                FindedNum(r6, 6)
 
 
        elif TargetRoom == 7:
            r7 = FindTemplate(template07)
            r7L = FindTemplate(template7L)
            r7LL = FindTemplate(template7LL)
            r7R = FindTemplate(template7R)
            r7RR = FindTemplate(template7RR)
 
            if r7L:
                FindedNum(r7L, 7)
            elif r7LL:
                FindedNum(r7LL, 7)
            elif r7R:
                FindedNum(r7R, 7)
            elif r7RR:
                FindedNum(r7RR, 7)
            elif r7:
                FindedNum(r7, 7)
 
        elif TargetRoom == 8:
            r8 = FindTemplate(template08)
            r8L = FindTemplate(template8L)
            r8LL = FindTemplate(template8LL)
            r8R = FindTemplate(template8R)
            r8RR = FindTemplate(template8RR)
 
            if r8L:
                FindedNum(r8L, 8)
            elif r8LL:
                FindedNum(r8LL, 8)
            elif r8R:
                FindedNum(r8R, 8)
            elif r8RR:
                FindedNum(r8RR, 8)
            elif r8:
                FindedNum(r8, 8)
 
        #else: time.sleep_ms(100)
    else: time.sleep_ms(100)
    print(clock.fps(),Find_Task, TargetRoom)