t = int(input())

while t:
    n = int(input())

    np = n
    while True:
        np += 1
        ntemp = np
        nrev = 0
        while ntemp > 0:
            ldig = int(ntemp % 10)
            nrev = nrev * 10 + ldig
            ntemp = ntemp // 10

        if nrev == np:
            break
    t -= 1
    print(np)
