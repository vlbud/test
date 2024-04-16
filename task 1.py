import random


def Massive():
    a = random.randint(2, 30)
    mas = [random.randint(0, 99) for i in range(a)]
    min = mas[0]
    max = mas[0]
    average = 0
    for i in range(1, len(mas)):
        if mas[i] > max:
            max = mas[i]
        if mas[i] < min:
            min = mas[i]
        average += i
    average = average / a
    print('Максимальное значение = ', max)
    print('Минимальное значение = ', min)
    print('Среднее значение = ', average)


Massive()
