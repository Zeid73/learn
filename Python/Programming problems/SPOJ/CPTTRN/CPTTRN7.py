t = int(input())

while t:
    tl = list(input().split())
    lm = int(tl[0])
    cm = int(tl[1])
    s = int(tl[2])

    for l in range(2 * s * lm):
        strtmp = str()
        for c in range(2 * s * cm):
            if abs(l - c) % (2 * s) == s:
                strtmp = strtmp + "\\"

            elif (l + c) % (2 * s) == s - 1:
                strtmp = strtmp + "/"
            else:
                strtmp = strtmp + "."

        print(strtmp)
    t -= 1
    print("")
