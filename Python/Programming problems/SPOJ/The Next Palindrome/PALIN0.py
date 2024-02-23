t = int(input())

while t:
    n = int(input())

    ln = [int(x) for x in str(n)]
    if n == int("9" * len(ln)):
        nx = n + 2
        print(nx)

    else:
        mid = len(ln) // 2
        i = mid - 1
        if len(ln) % 2 == 0:
            j = mid
        else:
            j = mid + 1

        while i >= 0 and ln[i] == ln[j]:
            i -= 1
            j += 1

        if i < 0 or ln[i] < ln[j]:
            lsmall = True
        else:
            lsmall = False

        while i >= 0:
            ln[j] = ln[i]
            i -= 1
            j += 1

        if lsmall:
            c = 1
            i = mid - 1
            if len(ln) % 2 != 0:
                ln[mid] = ln[mid] + c
                c = int(ln[mid] / 10)
                ln[mid] %= 10
                j = mid + 1
            else:
                j = mid
        else:
            c = int(ln[i] / 10)

        while i >= 0:
            ln[i] += c
            c = int(ln[i] / 10)
            ln[i] %= 10
            ln[j] = ln[i]
            i -= 1
            j += 1
        for a in ln:
            print(int(a), end="")
    t -= 1
    print()
