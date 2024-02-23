t = int(input())

while t:
    tl = list(input().split())
    lm = int(tl[0])
    cm = int(tl[1])
    s = int(tl[2])

    s1 = s + 1
    for l in range(s1 * lm + 1):
        strtmp = str()
        for c in range(s1 * cm + 1):
            if l == 0 or c == 0 or l % s1 == 0 or c % s1 == 0:
                strtmp = strtmp + "*"
            else:
                if (l // s1 + c // s1) % 2 == 0:
                    if l % s1 == c % s1:
                        strtmp = strtmp + "\\"
                    else:
                        strtmp = strtmp + "."
                else:
                    if l % s1 == s1 - c % s1:
                        strtmp = strtmp + "/"
                    else:
                        strtmp = strtmp + "."
        print(strtmp)
    t -= 1
    print("")
