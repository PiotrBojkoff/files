import RPi.GPIO as GPIO
from time import time_ns as time_ns

d2b = lambda x : list(map(int, f"0000000{x:b}"))[-8:]

GPIO.setmode(11)
dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()

print("Введи период колебаний (в наносекундах).")
t = float(input())
fac = 256/t
start = time_ns()

GPIO.setup(dac, 0)
try:
    while True:
        x = (time_ns()-start)%t * 2
        if x >= t: x = 2*t - x
        GPIO.output(dac, d2b(int(round(x)+0.1)))
except KeyboardInterrupt:
    print("\nВыполнение прервано пользователем.")
except:
    print("Непредвиденная несуразица.")
finally:
    GPIO.cleanup()