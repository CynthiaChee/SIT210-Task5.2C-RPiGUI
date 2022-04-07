from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

def led_red():
    if GPIO.input(11) == GPIO.HIGH:
        GPIO.output(11,GPIO.LOW)
        ledButton1["text"] = "Turn RED LED on"
    else:
        GPIO.output(11,GPIO.HIGH)
        ledButton1["text"] = "Turn RED LED off"

def led_green():
    if GPIO.input(13) == GPIO.HIGH:
        GPIO.output(13,GPIO.LOW)
        ledButton2["text"] = "Turn GREEN LED on"
    else:
        GPIO.output(13,GPIO.HIGH)
        ledButton2["text"] = "Turn GREEN LED off"

def led_blue():
    if GPIO.input(15) == GPIO.HIGH:
        GPIO.output(15,GPIO.LOW)
        ledButton3["text"] = "Turn BLUE LED on"
    else:
        GPIO.output(15,GPIO.HIGH)
        ledButton3["text"] = "Turn BLUE LED off"

ledButton1 = Button(win, text = "Turn RED LED on", font = myFont, command = led_red,bg = 'red', height = 1, width = 24)
ledButton2 = Button(win, text = "Turn GREEN LED on", font = myFont, command = led_green,bg = 'green', height = 1, width = 24)
ledButton3 = Button(win, text = "Turn BLUE LED on", font = myFont, command = led_blue,bg = 'blue', height = 1, width = 24)
ledButton1.grid(row=0, column=1)
ledButton2.grid(row=1, column=1)
ledButton3.grid(row=2, column=1)
