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
เนื่องจากบนบอร์ดมี LED จำนวน 3 ดวง 3 สี คือ สีแดงอยู่ที่ขา 22 สีเขียวอยู่ที่ขา 17 และ สีเหลืองอยู่ที่ขา 27 ดังนั้นจะเขียนโปรแกรมให้วนกระพริบดวงละ 0.5 วินาที 

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
