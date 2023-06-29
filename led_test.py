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
