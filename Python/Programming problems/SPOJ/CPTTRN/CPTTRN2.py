t = int(input())

while t:
    tl = list(input().split())
    lm = int(tl[0])
    cm = int(tl[1])

    for l in range(lm):
        strtmp = str()
        for c in range(cm):
            if l == 0 or c == 0 or l == lm - 1 or c == cm - 1:
                strtmp = strtmp + "*"
            else:
                strtmp = strtmp + "."
        print(strtmp)
    t -= 1
    print("")
