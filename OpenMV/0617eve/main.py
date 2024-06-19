import time, sensor, image,ustruct,struct
from pyb import UART,LED
from image import SEARCH_EX, SEARCH_DS
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
LED(1).on()
LED(2).on()
LED(3).on()
template1 = image.Image("/1.pgm")
template2 = image.Image("/2.pgm")
templates3 = ["/3.pgm","/3_1.pgm","/3_2.pgm","/3_3.pgm","/3_4.pgm","/3_5.pgm","/3_6.pgm","/3_7.pgm","/3_8.pgm","/r3_10.pgm","/r3_11.pgm","/r3_12.pgm","/r3_13.pgm","/r3_14.pgm","/3ll.pgm","/3l.pgm","/3r.pgm","/3rr.pgm"]
templates4 = ["/4.pgm","/4_1.pgm","/4_2.pgm","/4_3.pgm","/4_4.pgm","/4_5.pgm","/4_6.pgm","/4_7.pgm","/4_8.pgm","/r4_10.pgm","/r4_11.pgm","/r4_12.pgm","/r4_13.pgm","/r4_14.pgm","/4ll.pgm","/4l.pgm","/4r.pgm","/4rr.pgm"]
templates5 = ["/5.pgm","/5_1.pgm","/5_2.pgm","/5_3.pgm","/5_4.pgm","/5_5.pgm","/5_6.pgm","/5_7.pgm","/5_8.pgm","/r5_10.pgm","/r5_11.pgm","/r5_12.pgm","/r5_13.pgm","/r5_14.pgm","/5ll.pgm","/5l.pgm","/5r.pgm","/5rr.pgm"]
templates6 = ["/6.pgm","/6_1.pgm","/6_2.pgm","/6_3.pgm","/6_4.pgm","/6_5.pgm","/6_6.pgm","/6_7.pgm","/6_8.pgm","/r6_10.pgm","/r6_11.pgm","/r6_12.pgm","/r6_13.pgm","/r6_14.pgm","/6ll.pgm","/6l.pgm","/6r.pgm","/6rr.pgm"]
templates7 = ["/7.pgm","/7_1.pgm","/7_2.pgm","/7_3.pgm","/7_4.pgm","/7_5.pgm","/7_6.pgm","/7_7.pgm","/7_8.pgm","/r7_10.pgm","/r7_11.pgm","/r7_12.pgm","/r7_13.pgm","/r7_14.pgm","/7ll.pgm","/7l.pgm","/7r.pgm","/7rr.pgm"]
templates8 = ["/8.pgm","/8_1.pgm","/8_2.pgm","/8_3.pgm","/8_4.pgm","/8_5.pgm","/8_6.pgm","/8_7.pgm","/8_8.pgm","/r8_10.pgm","/r8_11.pgm","/r8_12.pgm","/r8_13.pgm","/r8_14.pgm","/8ll.pgm","/8l.pgm","/8r.pgm","/8rr.pgm"]
clock = time.clock()
uart = UART(3,115200)
uart.init(115200, bits=8, parity=None, stop=1)
def send_data(outn,lr,flag,task):
    global uart
    data=struct.pack("<bbbbbbb",0x2C,0x12,outn,lr,flag,task,0x5B)
    uart.write(data)
while (True):
    clock.tick()
    img = sensor.snapshot()
    num=0
    r1_0 = img.find_template(template1, 0.80, step=5, search=SEARCH_EX)
    if r1_0:
        print(r1_0)
        print('1')
        num=1
        send_data(1,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r2_0 = img.find_template(template2, 0.70, step=5, search=SEARCH_EX)
    if r2_0:
        print(r2_0)
        print('2')
        num=2
        send_data(2,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r3_0 = img.find_template(image.Image(templates3[0]), 0.80, step=5, search=SEARCH_EX)
    if r3_0:
        print(r3_0)
        print('3')
        num=3
        send_data(3,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r4_0 = img.find_template(image.Image(templates4[0]), 0.80, step=5, search=SEARCH_EX)
    if r4_0:
        print(r4_0)
        print('4')
        num=4
        send_data(4,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r5_0 = img.find_template(image.Image(templates5[0]), 0.80, step=5, search=SEARCH_EX)
    if r5_0:
        print(r5_0)
        print('5')
        num=5
        send_data(5,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r6_0 = img.find_template(image.Image(templates6[0]), 0.80, step=5, search=SEARCH_EX)
    if r6_0:
        print(r6_0)
        print('6')
        num=6
        send_data(6,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r7_0 = img.find_template(image.Image(templates7[0]), 0.80, step=5, search=SEARCH_EX)
    if r7_0:
        print(r7_0)
        print('7')
        num=7
        send_data(7,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r8_0 = img.find_template(image.Image(templates8[0]), 0.80, step=5, search=SEARCH_EX)
    if r8_0:
        print(r8_0)
        print('8')
        num=8
        send_data(8,0,1,2)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    if num!=0:

        while(True):
            clock.tick()
            img = sensor.snapshot()
            if num==1:
                send_data(1,0,1,2)
            if num==2:
                send_data(2,0,1,2)
            if num==3:
                r3_0 = img.find_template(image.Image(templates3[0]), 0.70, step=5, search=SEARCH_EX)
                if r3_0:
                    print(r3_0)
                    print('3')
                    send_data(num,int(r3_0[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_1 = img.find_template(image.Image(templates3[1]), 0.70, step=5, search=SEARCH_EX)
                if r3_1:
                    print(r3_1)
                    print('3')
                    send_data(num,int(r3_1[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_2 = img.find_template(image.Image(templates3[2]), 0.70, step=5, search=SEARCH_EX)
                if r3_2:
                    print(r3_2)
                    print('3')
                    send_data(num,int(r3_2[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_3 = img.find_template(image.Image(templates3[3]), 0.70, step=5, search=SEARCH_EX)
                if r3_3:
                    print(r3_3)
                    print('3')
                    send_data(num,int(r3_3[0])/65+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_4 = img.find_template(image.Image(templates3[4]), 0.70, step=5, search=SEARCH_EX)
                if r3_4:
                    print(r3_4)
                    print('3')
                    send_data(num,int(r3_4[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_5 = img.find_template(image.Image(templates3[5]), 0.70, step=5, search=SEARCH_EX)
                if r3_5:
                    print(r3_5)
                    print('3')
                    send_data(num,int(r3_5[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_6 = img.find_template(image.Image(templates3[6]), 0.70, step=5, search=SEARCH_EX)
                if r3_6:
                    print(r3_6)
                    print('3')
                    send_data(num,int(r3_6[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_7 = img.find_template(image.Image(templates3[7]), 0.70, step=5, search=SEARCH_EX)
                if r3_7:
                    print(r3_7)
                    print('3')
                    send_data(num,int(r3_7[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_8 = img.find_template(image.Image(templates3[8]), 0.70, step=5, search=SEARCH_EX)
                if r3_8:
                    print(r3_8)
                    print('3')
                    send_data(num,int(r3_8[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_10 = img.find_template(image.Image(templates3[9]), 0.70, step=5, search=SEARCH_EX)
                if r3_10:
                    print(r3_10)
                    print('3')
                    send_data(num,int(r3_10[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_11 = img.find_template(image.Image(templates3[10]), 0.70, step=5, search=SEARCH_EX)
                if r3_11:
                    print(r3_11)
                    print('3')
                    send_data(num,int(r3_11[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_12 = img.find_template(image.Image(templates3[11]), 0.70, step=5, search=SEARCH_EX)
                if r3_12:
                    print(r3_12)
                    print('3')
                    send_data(num,int(r3_12[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_13 = img.find_template(image.Image(templates3[12]), 0.70, step=5, search=SEARCH_EX)
                if r3_13:
                    print(r3_13)
                    print('3')
                    send_data(num,int(r3_13[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_14 = img.find_template(image.Image(templates3[13]), 0.70, step=5, search=SEARCH_EX)
                if r3_14:
                    print(r3_14)
                    print('3')
                    send_data(num,int(r3_14[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)



            if num==4:
                r4_0 = img.find_template(image.Image(templates4[0]), 0.70, step=5, search=SEARCH_EX)
                if r4_0:
                    print(r4_0)
                    print('4')
                    send_data(num,int(r4_0[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_1 = img.find_template(image.Image(templates4[1]), 0.70, step=5, search=SEARCH_EX)
                if r4_1:
                    print(r4_1)
                    print('4')
                    send_data(num,int(r4_1[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_2 = img.find_template(image.Image(templates4[2]), 0.70, step=5, search=SEARCH_EX)
                if r4_2:
                    print(r4_2)
                    print('4')
                    send_data(num,int(r4_2[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_3 = img.find_template(image.Image(templates4[3]), 0.70, step=5, search=SEARCH_EX)
                if r4_3:
                    print(r4_3)
                    print('4')
                    send_data(num,int(r4_3[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_4 = img.find_template(image.Image(templates4[4]), 0.70, step=5, search=SEARCH_EX)
                if r4_4:
                    print(r4_4)
                    print('4')
                    send_data(num,int(r4_4[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_5 = img.find_template(image.Image(templates4[5]), 0.70, step=5, search=SEARCH_EX)
                if r4_5:
                    print(r4_5)
                    print('4')
                    send_data(num,int(r4_5[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_6 = img.find_template(image.Image(templates4[6]), 0.70, step=5, search=SEARCH_EX)
                if r4_6:
                    print(r4_6)
                    print('4')
                    send_data(num,int(r4_6[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_7 = img.find_template(image.Image(templates4[7]), 0.70, step=5, search=SEARCH_EX)
                if r4_7:
                    print(r4_7)
                    print('4')
                    send_data(num,int(r4_7[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_8 = img.find_template(image.Image(templates4[8]), 0.70, step=5, search=SEARCH_EX)
                if r4_8:
                    print(r4_8)
                    print('4')
                    send_data(num,int(r4_8[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_10 = img.find_template(image.Image(templates4[9]), 0.70, step=5, search=SEARCH_EX)
                if r4_10:
                    print(r4_10)
                    print('4')
                    send_data(num,int(r4_10[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_11 = img.find_template(image.Image(templates4[10]), 0.70, step=5, search=SEARCH_EX)
                if r4_11:
                    print(r4_11)
                    print('4')
                    send_data(num,int(r4_11[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_12 = img.find_template(image.Image(templates4[11]), 0.70, step=5, search=SEARCH_EX)
                if r4_12:
                    print(r4_12)
                    print('4')
                    send_data(num,int(r4_12[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_13 = img.find_template(image.Image(templates4[12]), 0.70, step=5, search=SEARCH_EX)
                if r4_13:
                    print(r4_13)
                    print('4')
                    send_data(num,int(r4_13[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_14 = img.find_template(image.Image(templates4[13]), 0.70, step=5, search=SEARCH_EX)
                if r4_14:
                    print(r4_14)
                    print('4')
                    send_data(num,int(r4_14[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)


            if num==5:
                r5_0 = img.find_template(image.Image(templates5[0]), 0.70, step=5, search=SEARCH_EX)
                if r5_0:
                    print(r5_0)
                    print('5')
                    send_data(num,int(r5_0[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_1 = img.find_template(image.Image(templates5[1]), 0.70, step=5, search=SEARCH_EX)
                if r5_1:
                    print(r5_1)
                    print('5')
                    send_data(num,int(r5_1[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_2 = img.find_template(image.Image(templates5[2]), 0.70, step=5, search=SEARCH_EX)
                if r5_2:
                    print(r5_2)
                    print('5')
                    send_data(num,int(r5_2[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_3 = img.find_template(image.Image(templates5[3]), 0.70, step=5, search=SEARCH_EX)
                if r5_3:
                    print(r5_3)
                    print('5')
                    send_data(num,int(r5_3[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_4 = img.find_template(image.Image(templates5[4]), 0.70, step=5, search=SEARCH_EX)
                if r5_4:
                    print(r5_4)
                    print('5')
                    send_data(num,int(r5_4[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_5 = img.find_template(image.Image(templates5[5]), 0.70, step=5, search=SEARCH_EX)
                if r5_5:
                    print(r5_5)
                    print('5')
                    send_data(num,int(r5_5[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_6 = img.find_template(image.Image(templates5[6]), 0.70, step=5, search=SEARCH_EX)
                if r5_6:
                    print(r5_6)
                    print('5')
                    send_data(num,int(r5_6[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_7 = img.find_template(image.Image(templates5[7]), 0.70, step=5, search=SEARCH_EX)
                if r5_7:
                    print(r5_7)
                    print('5')
                    send_data(num,int(r5_7[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_8 = img.find_template(image.Image(templates5[8]), 0.70, step=5, search=SEARCH_EX)
                if r5_8:
                    print(r5_8)
                    print('5')
                    send_data(num,int(r5_8[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_10 = img.find_template(image.Image(templates5[9]), 0.70, step=5, search=SEARCH_EX)
                if r5_10:
                    print(r5_10)
                    print('5')
                    send_data(num,int(r5_10[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_11 = img.find_template(image.Image(templates5[10]), 0.70, step=5, search=SEARCH_EX)
                if r5_11:
                    print(r5_11)
                    print('5')
                    send_data(num,int(r5_11[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_12 = img.find_template(image.Image(templates5[11]), 0.70, step=5, search=SEARCH_EX)
                if r5_12:
                    print(r5_12)
                    print('5')
                    send_data(num,int(r5_12[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_13 = img.find_template(image.Image(templates5[12]), 0.70, step=5, search=SEARCH_EX)
                if r5_13:
                    print(r5_13)
                    print('5')
                    send_data(num,int(r5_13[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_14 = img.find_template(image.Image(templates5[13]), 0.70, step=5, search=SEARCH_EX)
                if r5_14:
                    print(r5_14)
                    print('5')
                    send_data(num,int(r5_14[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)


            if num==6:
                r6_0 = img.find_template(image.Image(templates6[0]), 0.70, step=5, search=SEARCH_EX)
                if r6_0:
                    print(r6_0)
                    print('6')
                    send_data(num,int(r6_0[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_1 = img.find_template(image.Image(templates6[1]), 0.70, step=5, search=SEARCH_EX)
                if r6_1:
                    print(r6_1)
                    print('6')
                    send_data(num,int(r6_1[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_2 = img.find_template(image.Image(templates6[2]), 0.70, step=5, search=SEARCH_EX)
                if r6_2:
                    print(r6_2)
                    print('6')
                    send_data(num,int(r6_2[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_3 = img.find_template(image.Image(templates6[3]), 0.70, step=5, search=SEARCH_EX)
                if r6_3:
                    print(r6_3)
                    print('6')
                    send_data(num,int(r6_3[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_4 = img.find_template(image.Image(templates6[4]), 0.70, step=5, search=SEARCH_EX)
                if r6_4:
                    print(r6_4)
                    print('6')
                    send_data(num,int(r6_4[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_5 = img.find_template(image.Image(templates6[5]), 0.70, step=5, search=SEARCH_EX)
                if r6_5:
                    print(r6_5)
                    print('6')
                    send_data(num,int(r6_5[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_6 = img.find_template(image.Image(templates6[6]), 0.70, step=5, search=SEARCH_EX)
                if r6_6:
                    print(r6_6)
                    print('6')
                    send_data(num,int(r6_6[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_7 = img.find_template(image.Image(templates6[7]), 0.70, step=5, search=SEARCH_EX)
                if r6_7:
                    print(r6_7)
                    print('6')
                    send_data(num,int(r6_7[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_8 = img.find_template(image.Image(templates6[8]), 0.70, step=5, search=SEARCH_EX)
                if r6_8:
                    print(r6_8)
                    print('6')
                    send_data(num,int(r6_8[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_10 = img.find_template(image.Image(templates6[9]), 0.70, step=5, search=SEARCH_EX)
                if r6_10:
                    print(r6_10)
                    print('6')
                    send_data(num,int(r6_10[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_11 = img.find_template(image.Image(templates6[10]), 0.70, step=5, search=SEARCH_EX)
                if r6_11:
                    print(r6_11)
                    print('6')
                    send_data(num,int(r6_11[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_12 = img.find_template(image.Image(templates6[11]), 0.70, step=5, search=SEARCH_EX)
                if r6_12:
                    print(r6_12)
                    print('6')
                    send_data(num,int(r6_12[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_13 = img.find_template(image.Image(templates6[12]), 0.70, step=5, search=SEARCH_EX)
                if r6_13:
                    print(r6_13)
                    print('6')
                    send_data(num,int(r6_13[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_14 = img.find_template(image.Image(templates6[13]), 0.70, step=5, search=SEARCH_EX)
                if r6_14:
                    print(r6_14)
                    print('6')
                    send_data(num,int(r6_14[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)


            if num==7:
                r7_0 = img.find_template(image.Image(templates7[0]), 0.80, step=5, search=SEARCH_EX)
                if r7_0:
                    print(r7_0)
                    print('7')
                    send_data(num,int(r7_0[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_1 = img.find_template(image.Image(templates7[1]), 0.80, step=5, search=SEARCH_EX)
                if r7_1:
                    print(r7_1)
                    print('7')
                    send_data(num,int(r7_1[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_2 = img.find_template(image.Image(templates7[2]), 0.80, step=5, search=SEARCH_EX)
                if r7_2:
                    print(r7_2)
                    print('7')
                    send_data(num,int(r7_2[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_3 = img.find_template(image.Image(templates7[3]), 0.80, step=5, search=SEARCH_EX)
                if r7_3:
                    print(r7_3)
                    print('7')
                    send_data(num,int(r7_3[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_4 = img.find_template(image.Image(templates7[4]), 0.80, step=5, search=SEARCH_EX)
                if r7_4:
                    print(r7_4)
                    print('7')
                    send_data(num,int(r7_4[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_5 = img.find_template(image.Image(templates7[5]), 0.80, step=5, search=SEARCH_EX)
                if r7_5:
                    print(r7_5)
                    print('7')
                    send_data(num,int(r7_5[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_6 = img.find_template(image.Image(templates7[6]), 0.80, step=5, search=SEARCH_EX)
                if r7_6:
                    print(r7_6)
                    print('7')
                    send_data(num,int(r7_6[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_7 = img.find_template(image.Image(templates7[7]), 0.80, step=5, search=SEARCH_EX)
                if r7_7:
                    print(r7_7)
                    print('7')
                    send_data(num,int(r7_7[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_8 = img.find_template(image.Image(templates7[8]), 0.80, step=5, search=SEARCH_EX)
                if r7_8:
                    print(r7_8)
                    print('7')
                    send_data(num,int(r7_8[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_10 = img.find_template(image.Image(templates7[9]), 0.80, step=5, search=SEARCH_EX)
                if r7_10:
                    print(r7_10)
                    print('7')
                    send_data(num,int(r7_10[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_11 = img.find_template(image.Image(templates7[10]), 0.80, step=5, search=SEARCH_EX)
                if r7_11:
                    print(r7_11)
                    print('7')
                    send_data(num,int(r7_11[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_12 = img.find_template(image.Image(templates7[11]), 0.80, step=5, search=SEARCH_EX)
                if r7_12:
                    print(r7_12)
                    print('7')
                    send_data(num,int(r7_12[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_13 = img.find_template(image.Image(templates7[12]), 0.80, step=5, search=SEARCH_EX)
                if r7_13:
                    print(r7_13)
                    print('7')
                    send_data(num,int(r7_13[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_14 = img.find_template(image.Image(templates7[13]), 0.80, step=5, search=SEARCH_EX)
                if r7_14:
                    print(r7_14)
                    print('7')
                    send_data(num,int(r7_14[0]/65)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)


            if num==8:
                r8_0 = img.find_template(image.Image(templates8[0]), 0.70, step=5, search=SEARCH_EX)
                if r8_0:
                    print(r8_0)
                    print('8')
                    send_data(num,int(r8_0[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_1 = img.find_template(image.Image(templates8[1]), 0.70, step=5, search=SEARCH_EX)
                if r8_1:
                    print(r8_1)
                    print('8')
                    send_data(num,int(r8_1[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_2 = img.find_template(image.Image(templates8[2]), 0.70, step=5, search=SEARCH_EX)
                if r8_2:
                    print(r8_2)
                    print('8')
                    send_data(num,int(r8_2[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_3 = img.find_template(image.Image(templates8[3]), 0.70, step=5, search=SEARCH_EX)
                if r8_3:
                    print(r8_3)
                    print('8')
                    send_data(num,int(r8_3[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_4 = img.find_template(image.Image(templates8[4]), 0.70, step=5, search=SEARCH_EX)
                if r8_4:
                    print(r8_4)
                    print('8')
                    send_data(num,int(r8_4[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_5 = img.find_template(image.Image(templates8[5]), 0.70, step=5, search=SEARCH_EX)
                if r8_5:
                    print(r8_5)
                    print('8')
                    send_data(num,int(r8_5[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_6 = img.find_template(image.Image(templates8[6]), 0.70, step=5, search=SEARCH_EX)
                if r8_6:
                    print(r8_6)
                    print('8')
                    send_data(num,int(r8_6[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_7 = img.find_template(image.Image(templates8[7]), 0.70, step=5, search=SEARCH_EX)
                if r8_7:
                    print(r8_7)
                    print('8')
                    send_data(num,int(r8_7[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_8 = img.find_template(image.Image(templates3[8]), 0.70, step=5, search=SEARCH_EX)
                if r8_8:
                    print(r8_8)
                    print('8')
                    send_data(num,int(r8_8[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_10 = img.find_template(image.Image(templates8[9]), 0.70, step=5, search=SEARCH_EX)
                if r8_10:
                    print(r8_10)
                    print('8')
                    send_data(num,int(r8_10[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_11 = img.find_template(image.Image(templates8[10]), 0.70, step=5, search=SEARCH_EX)
                if r8_11:
                    print(r8_11)
                    print('8')
                    send_data(num,int(r8_11[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_12 = img.find_template(image.Image(templates8[11]), 0.70, step=5, search=SEARCH_EX)
                if r8_12:
                    print(r8_12)
                    print('8')
                    send_data(num,int(r8_12[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_13 = img.find_template(image.Image(templates8[12]), 0.70, step=5, search=SEARCH_EX)
                if r8_13:
                    print(r8_13)
                    print('8')
                    send_data(num,int(r8_13[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_14 = img.find_template(image.Image(templates8[13]), 0.70, step=5, search=SEARCH_EX)
                if r8_14:
                    print(r8_14)
                    print('8')
                    send_data(num,int(r8_14[0]/70)+1,1,2)

                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)

