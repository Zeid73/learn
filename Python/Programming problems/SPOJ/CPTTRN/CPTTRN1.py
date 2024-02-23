t = int(input())

while t:
    tl = list(input().split())
    lm = int(tl[0])
    cm = int(tl[1])

    mod = True
    for l in range(lm):
        strtmp = str()
        for c in range(cm):
            if mod:
                strtmp = strtmp + "*"
            else:
                strtmp = strtmp + "."
            mod = not mod
        if (cm % 2) == 0:
            mod = not mod
        print(strtmp)
    t -= 1
    print()
