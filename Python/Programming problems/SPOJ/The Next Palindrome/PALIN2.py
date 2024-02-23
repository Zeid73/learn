t = int(input())

while t:
    n = int(input())
    sn = str(n)

    # if sn == "9" * len(sn):
    #     n = n + 2
    #     print(n)

    if len(sn) % 2 != 0:
        lhalf = sn[: len(sn) // 2 + 1]
        c = int(lhalf + lhalf[-2::-1])
        if c > n:
            print(c)
        else:
            nlhalf = str(int(lhalf) + 1)
            if len(nlhalf) == len(lhalf):
                print(int(nlhalf + nlhalf[-2::-1]))
            else:
                print(10 ** len(sn) + 1)
    else:
        lhalf = sn[: len(sn) // 2]
        c = int(lhalf + lhalf[::-1])
        if c > n:
            print(c)
        else:
            nlhalf = str(int(lhalf) + 1)
            if len(nlhalf) == len(lhalf):
                print(nlhalf + nlhalf[::-1])
            else:
                print(10 ** len(sn) + 1)

    t -= 1
