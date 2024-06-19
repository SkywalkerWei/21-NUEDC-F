# Edge Impulse - OpenMV Image Classification Example

import sensor, image, time, os, tf

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)      # Set frame size to QVGA (320x240)
#sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net4 = "trained4.tflite"
labels4 = [line.rstrip('\n') for line in open("labels4.txt")]

clock = time.clock()
while(True):
    clock.tick()

    img = sensor.snapshot()
    roiL1=(7,60,20,20)

    for obj in tf.classify(net4, img, roiL1,min_scale=1, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())

        predictions_list = list(zip(labels4, obj.output()))
    for i in range(len(predictions_list)):
        print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

    roiR1=(89,56,24,22)
    for obj in tf.classify(net4, img, roiR1,min_scale=1, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions2 at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())

        predictions_list2 = list(zip(labels4, obj.output()))
    for p in range(len(predictions_list2)):
        print("%s = %f" % (predictions_list2[p][0], predictions_list2[p][1]))

    print(clock.fps(), "fps")
