t = int(input())

while t:
    tl = list(input().split())
    lm = int(tl[0])
    cm = int(tl[1])
    h = int(tl[2])
    w = int(tl[3])

    for l in range(1, lm + (lm + 1) * h + 1):
        strtmp = str()
        for c in range(1, cm + (cm + 1) * w + 1):
            if l % (h + 1) == 0 and c % (w + 1) == 0:
                strtmp = strtmp + "+"
            elif c % (w + 1) == 0:
                strtmp = strtmp + "|"
            elif l % (h + 1) == 0:
                strtmp = strtmp + "-"
            else:
                strtmp = strtmp + "."
        print(strtmp)
    t -= 1
    print("")
