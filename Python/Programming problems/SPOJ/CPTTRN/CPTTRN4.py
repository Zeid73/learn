t = int(input())
s = list(str(range(t)))

for i in range(t):
    s[i] = input()

# print("\n", "-" * 20, "\n")

for i in range(t):
    tl = s[i].split()
    lm = int(tl[0])
    cm = int(tl[1])
    h = int(tl[2])
    w = int(tl[3])

    for l in range((h + 1) * lm + 1):
        strtmp = str()
        for c in range((w + 1) * cm + 1):
            if l == 0 or c == 0 or l % (h + 1) == 0 or c % (w + 1) == 0:
                strtmp = strtmp + "*"
            else:
                strtmp = strtmp + "."
        print(strtmp)

    print("")
