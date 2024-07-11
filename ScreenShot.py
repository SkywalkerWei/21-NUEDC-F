import sensor,time,image
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
while (1):
    img = sensor.snapshot()
    time.sleep_ms(10)
