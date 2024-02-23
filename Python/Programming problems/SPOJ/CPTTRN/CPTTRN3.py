t = int(input())

while t:
    tl = list(input().split())
    lm = int(tl[0])
    cm = int(tl[1])

    for l in range(3 * lm + 1):
        strtmp = str()
        for c in range(3 * cm + 1):
            if l == 0 or c == 0 or l % 3 == 0 or c % 3 == 0:
                strtmp = strtmp + "*"
            else:
                strtmp = strtmp + "."
        print(strtmp)
    t -= 1
    print()
