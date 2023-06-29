# Easy-EIoT
ทดสอบบอร์ด Easy-EIoT

ได้ซื้อบอร์ด Easy-eIoT HAT สำหรับใช้ต่อเข้ากับบอร์ด Raspberry Pi มาบอร์ดหนึ่ง 
บนบอร์ดประกอบด้วย

1. จอสี  IPS LCD ขนาด 1.54" ความละเอียด 240x240 ให้มุมมองกว้างสีสันสดใส สามารถตั้งค่าให้เป็น frame buffer ได้เลย
2. ปุ่ม Rotary Encoder สำหรับใช้ในงานควบคุมสามารถหมุนซ้ายขวาและกดเป็นปุ่มได้
3. ปุ่มกด ขนาดใหญ่ 15mm สำหรับใช้กดเพื่อสั่งการทำงานตามที่ต้องการ
4. Buzzer สำหรับส่งเสียงการทำงานต่างๆให้เสียงดังชัดเจนสามารถควบคุมความถี่เสียงได้ด้วยตัวเอง
5. LED 3 สี แดง เหลือง เขียว สำหรับใช้แสดงผลสถานะการทำงานต่างๆตามที่ต้องการ
6. RGB LED WS2812b สำหรับแสดงค่าสี RGB ภายในหลอดเดียวและสามารถต่อเชื่อมหลอดภายนอกได้ผ่าน connector ที่มีเตรียมไว้ให้แล้ว
7. เซ็นเซอร์วัดค่าความชื้นความชื้นสัมพัทธ์และอุณหภูมิแบบใช้ในงานอุตสาหกรรมเบอร์ HS3004 จาก Renesas (เฉพาะในรุ่น Easy-eIoT)
8. Pin header แยกสำหรับการเชื่อมต่อแบบต่างๆ ป้องกันความผิดพลาดจากการนับขา - Serial - I2C - SPI - I2S - 1-Wire

บทความนี้จึงจะมาทดสอบบอร์ดนี้กัน 

### ทดสอบ LED 
เนื่องจากบนบอร์ดมี LED จำนวน 3 ดวง 3 สี คือ สีแดงอยู่ที่ขา 22 สีเขียวอยู่ที่ขา 17 และ สีเหลืองอยู่ที่ขา 27 ดังนั้นจะเขียนโปรแกรมให้วนกระพริบดวงละ 0.5 วินาที โดยมีโปรแกรมดังนี้

```Python
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)


while(1):
    if time() - start_blink >  0.5 :
        start_blink = time()
        if led_counter == 0 :
            GPIO.output(red_pin, GPIO.LOW)
        else :
            GPIO.output(red_pin, GPIO.HIGH)

        if led_counter == 1 :
            GPIO.output(yellow_pin, GPIO.LOW)
        else :
            GPIO.output(yellow_pin, GPIO.HIGH)

        if led_counter == 2 :
            GPIO.output(green_pin, GPIO.LOW)
        else :
            GPIO.output(green_pin, GPIO.HIGH)

        if led_counter<2 :
            led_counter+=1
        else :
            led_counter=0
```

### ทดสอบสวิตซ์ Push Button 
เนื่องจากบนบอร์ดมีปุ่ม Push Button อยู่ 1 ปุ่ม โดยอยู่ที่ขา 26 จึงเขียนโปรแกรมให้นับจำนวนครั้งที่มีการกด โดยจะตรวจสอบการกดโดยใช้ ขอบขาลง (Falling Edge) และหากมีการกดให้ไปทำงานในฟังก์ชัน press_sw โดยมีโปรแกรมดังนี้

```Python

from RPi import GPIO
from time import sleep

press_sw_pin = 26
press_sw_counter = 0

def press_sw_callback(channel):
    global press_sw_counter
    press_sw_counter += 1
    print("Button switch press "+str(press_sw_counter)+" times")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(press_sw_pin, GPIO.IN)
GPIO.add_event_detect(press_sw_pin, GPIO.FALLING , callback=press_sw_callback, bouncetime=300)

print("Press button switch to increase counter")
while(1):
    sleep(0.1)
```

### ทดสอบ NeoPixel 
เนื่องจากบนบอร์ดมีไฟ NeoPixel อยู่ 1 ดวง คราวนี้เราจะใช้ Library โดยต้องติดตั้งก่อน โดยใช้คำสั่ง pip install rpi_ws281x 

### ทดสอบ Buzzer 
เนื่องจากบนบอร์ดมี Buzzer จำนวน 1 ตัว โดยอยู่ที่ pin 13 ในโปรแกรมจะใช้วิธีง่ายๆ คือ กำหนดความถี่ของ PWM ที่ pin นั้น และหน่วงเวลา โดยมีโปรแกรมดังนี้

```Python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

buzzer_pin=13
speed = 0.1
c4 = 261
d4 = 294
e4 = 329
f4 = 349
g4 = 392
a4 = 440
b4 = 493
c5 = 523.25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.output(buzzer_pin, True)

p = GPIO.PWM(buzzer_pin, 100) # start at freq 100Hz
p.start(50)#duty cycle 50%

p.ChangeFrequency(c4)
time.sleep(speed)
p.ChangeFrequency(d4)
time.sleep(speed)
p.ChangeFrequency(e4)
time.sleep(speed)
p.ChangeFrequency(f4)
time.sleep(speed)
p.ChangeFrequency(g4)
time.sleep(speed)
p.ChangeFrequency(a4)
time.sleep(speed)
p.ChangeFrequency(b4)
time.sleep(speed)
p.ChangeFrequency(c5)
time.sleep(speed)

p.stop()
GPIO.cleanup()
```


