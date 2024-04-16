def ugol():
    hours = int(input('Введите время в часах'))
    minutes = int(input('Введите время в минутах'))
    a = 360 / 12 * hours + 360 / 12 / 60 * minutes
    b = 360 / 60 * minutes
    while a > 360:
        a -= 360
    while b > 360:
        b -= 360
    x = abs(a - b)
    if x >= 180:
        x = abs(x - 360)
    print(x)


ugol()
