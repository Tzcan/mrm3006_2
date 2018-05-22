from PIL import Image
import pytesseract
import os
import picamera
import I2C_LCD_driver
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
i=1
mylcd = I2C_LCD_driver.lcd()
cd /home/pi/Desktop/foto
while=1:
	if GPIO.input(11)=0: #Giriş Sensörü
		with picamera.PiCamera() as camera:
			camera.captue('/home/pi/Desktop/foto/giris.jpg'.format(i))
			filename = "giris.jpg"
			giris_adi{i} = pytesseract.image_to_string(Image.open(filename))
			mv giris.jpg giris_adi[i].jpg
			mkdir /home/pi/Desktop/foto/giris_adi[i]
			mylcd.lcd_display_string("giris_adi[i]", 1, 1)
			mylcd.lcd_display_string("Hosgeldiniz", 2, 1)
			time.sleep(10)
			mylcd.lcd_clear()
			i+=1
			if i>100:
				i==0

			time.sleep(5)

	if GPIO.input(12)=0: #Çıkış Sensörü
		with picamera.PiCamera() as camera:
			camera.capture('home/pi/Desktop/foto/cikis.jpg'.format(i))
			filename = 'cikis.jpg'
			cikis_adi{i} = pytesseract.image_to_string(Image.open(filename))
			mv cikis.jpg cikis_adi[i]
			mylcd.lcd_display_string("giris_adi[i]")
			mylcd.lcd_display_string("{} TL",giris_zamani-cikis_zamani)
			time.sleep(10)
			mylcd.lcd_clear()
			rm giris_adi{i}
			rm cikis_adi{i}

			time.sleep(5)

