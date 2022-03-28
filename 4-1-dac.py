import RPi.GPIO as GPIO

d2b = lambda x : list(map(int, f"0000000{x:b}"))[-8:]

GPIO.setmode(11)
dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()

GPIO.setup(dac, 0)
try:
    while True:
        print("Введи число от 0 до 255 (q -- выход):")
        x = input()
        if x == "q":
            print("Прекращение работы.")
            break
        try:
            float(x)
        except:
            print("Нечисловое значение.")
            GPIO.output(dac, 0)
            continue
        try:
            x = int(x)
        except:
            print("Нецелое значение.")
            GPIO.output(dac, 0)
            continue
        if x<0:
            print("Отрицательное значение.")
            GPIO.output(dac, 0)
            continue
        if x>255:
            print("Значение вне допустимого (двоичного восьмиразрядного) промежутка.")
            GPIO.output(dac, 0)
            continue
        print(f"Подаётся напряжение {3.3*x/256:.5} В.")
        GPIO.output(dac, d2b(x))
except:
    print("Непредвиденная несуразица.")
finally:
    GPIO.cleanup()
