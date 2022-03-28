import RPi.GPIO as GPIO

d2b = lambda x : list(map(int, f"0000000{x:b}"))[-8:]

GPIO.setmode(11)
print("Введи способ работы (1 -- светлячок, 2 -- цепь)")
x = int(input())
if x==1:
    pin=21
elif x==2:
    pin = [26, 19, 13, 6, 5, 11, 9, 10]
else:
    raise ValueError

GPIO.setup(pin, 0)
schim = GPIO.PWM(pin, 50)
schim.start(0)

try:
    while True:
        print("Введи долю (0--100) заполненности промежутка:")
        x = int(input())
        if x<0 or x>100:
            print("Доля должна быть от 0 до 100.")
            continue
        schim.ChangeDutyCycle(x)
except ValueError:
    print("Введённое значение не может быть использовано.")
except:
    print("Непредвиденная несуразица.")
finally:
    GPIO.cleanup()