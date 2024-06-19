import time, sensor, image,os,tf
from image import SEARCH_EX, SEARCH_DS
from pyb import UART
from pyb import LED
import struct
uart = UART(3,115200)
uart.init(115200,bits=8,parity=None,stop=1)
sensor.reset()
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_windowing(0,50,160,70)
red_led   = LED(1)
green_led = LED(2)
blue_led  = LED(3)
ir_led	= LED(4)
green_led.on()
time.sleep_ms(500)
green_led.off()
net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]
template1 = ["/1.pgm","/1a.pgm","/1b.pgm"]
template2 = ["/2.pgm","/2a.pgm","/2b.pgm"]
template3 = ["/3.pgm","/3a.pgm","/3b.pgm","/3c.pgm","/3d.pgm"]
template4 = ["/4.pgm","/4a.pgm","/4b.pgm"]
template5 = ["/5.pgm","/5a.pgm","/5b.pgm"]
template6 = ["/6.pgm","/6a.pgm","/6b.pgm"]
template7 = ["/7.pgm","/7a.pgm","/7b.pgm"]
template8 = ["/8.pgm","/8a.pgm","/8b.pgm"]
A0=1
A9=1
B0=1
A1=0
A2=0
A3=0
A4=0
A5=0
A6=0
A7=0
A8=0
B0=1
C0=1
C1=0
D0=0
Find_task=0
find_flag=0
def send_data(outn,lr,flag,task):
    global uart
    data=struct.pack("<bbbbbbb",0x2C,0x12,outn,lr,flag,task,0x5B)
    uart.write(data)
clock = time.clock()
while (True):
        clock.tick()
        img = sensor.snapshot().lens_corr(strength = 1.8, zoom = 1.0)
        while(A0):
            clock.tick()
            img = sensor.snapshot()
            t1 = image.Image(template1[0])
            r1 = img.find_template(t1, 0.80, step=4, search=SEARCH_EX)
            if r1:
                img.draw_rectangle(r1)
                print('1')
                A1=1
                A0=0
            t2 = image.Image(template2[0])
            r2 = img.find_template(t2, 0.80, step=4, search=SEARCH_EX)
            if r2:
                img.draw_rectangle(r2)
                print('2')
                A2=1
                A0=0
            t3 = image.Image(template3[0])
            r3 = img.find_template(t3, 0.80, step=4, search=SEARCH_EX)
            if r3:
                img.draw_rectangle(r3)
                print('3')
                A3=1
                A0=0
            t4 = image.Image(template4[0])
            r4 = img.find_template(t4, 0.80, step=4, search=SEARCH_EX)
            if r4:
                img.draw_rectangle(r4)
                print('4')
                A4=1
                A0=0
            t5 = image.Image(template5[0])
            r5 = img.find_template(t5, 0.80, step=4, search=SEARCH_EX)
            if r5:
                img.draw_rectangle(r5)
                print('5')
                A5=1
                A0=0
            t6 = image.Image(template6[0])
            r6 = img.find_template(t6, 0.80, step=4, search=SEARCH_EX)
            if r6:
                img.draw_rectangle(r6)
                print('6')
                A6=1
                A0=0
            t7 = image.Image(template7[0])
            r7 = img.find_template(t7, 0.80, step=4, search=SEARCH_EX)
            if r7:
                img.draw_rectangle(r7)
                print('7')
                A7=1
                A0=0
            t8 = image.Image(template8[0])
            r8 = img.find_template(t8, 0.80, step=4, search=SEARCH_EX)
            if r8:
                img.draw_rectangle(r8)
                print('8')
                A8=1
                A0=0
        while(A9):
            if A1==1:
                send_data(1,0,1,2)
                print('1')
                num=1
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A2==1:
                send_data(2,0,1,2)
                print('2')
                num=2
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A3==1:
                send_data(3,0,1,2)
                print('3')
                num=3
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A4==1:
                send_data(4,0,1,2)
                print('4')
                num=4
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A5==1:
                send_data(5,0,1,2)
                print('5')
                num=5
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A6==1:
                send_data(6,0,1,2)
                print('6')
                num=6
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A7==1:
                send_data(7,0,1,2)
                print('7')
                num=7
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
            if A8==1:
                send_data(8,0,1,2)
                print('8')
                num=8
                A9=0
                green_led.on()
                time.sleep_ms(500)
                green_led.off()
        sended=0
        while(True):

            while(C0):
                img = sensor.snapshot()
                roiL=(15,0,50,50)
                for obj in tf.classify(net, img, roi=roiL,min_scale=1, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
                    print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
                    img.draw_rectangle(obj.rect())
                    predictions_list = list(zip(labels, obj.output()))
                for i in range(len(predictions_list)):
                    print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))
                    num1=ord(predictions_list[i][0])-48
                    if predictions_list[i][1]>0.7 and num1==num:
                        red_led.on()
                        time.sleep_ms(500)
                        red_led.off()
                        if sended==0:
                            send_data(num,1,1,2)
                            sended=5
                        else:
                            sended-=1
                        print('Left')
                        B0=1
                        C1=1

                roiR=(95,0,50,50)
                for obj in tf.classify(net, img, roi=roiR,min_scale=1, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
                    print("**********\nPredictions2 at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
                    img.draw_rectangle(obj.rect())
                    predictions_list2 = list(zip(labels, obj.output()))
                for p in range(len(predictions_list2)):
                    print("%s = %f" % (predictions_list2[p][0], predictions_list2[p][1]))
                    num2=ord(predictions_list2[p][0])-48
                    if predictions_list2[p][1]>0.7 and num2 == num:
                        blue_led.on()
                        time.sleep_ms(500)
                        blue_led.off()
                        if sended==0:
                            send_data(num,2,1,2)
                            sended=5
                        else:
                            sended-=1
                        print("Right")
                        B0=1
                        C1=1

                if C1==0:
                    send_data(num,0,0,2)
                    print("Straight")
                    B0=1
                time.sleep_ms(100)
