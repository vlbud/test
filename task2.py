def povtor():
    a = 'Hello'
    b = list(a.lower())
    y = []
    for i in range(len(a)):
        x = b[i]
        b.remove(b[i])
        if x in b:
            y.append(x)
        b = list(a)
    print(*set(y))


povtor()
