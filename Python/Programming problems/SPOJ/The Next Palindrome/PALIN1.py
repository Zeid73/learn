t = int(input())

while t:
    n = int(input())

    ln = list(map(int, str(n)))
    # if n == int("9" * len(ln)):
    #     n = n + 2
    #     print(n)

    # else:
    mid = len(ln) // 2
    i = mid - 1
    j = mid + 1 if len(ln) % 2 != 0 else mid

    while i >= 0 and ln[i] == ln[j]:
        i -= 1
        j += 1

    c = 0
    if i < 0 or ln[i] < ln[j]:
        c = 1
        i = mid - 1
        if len(ln) % 2 != 0:
            ln[mid] += c
            c = ln[mid] // 10
            ln[mid] %= 10
            j = mid + 1
        else:
            j = mid

    while i >= 0:
        if c != 0:
            ln[i] += c
            c = ln[i] // 10
            ln[i] %= 10
        ln[j] = ln[i]
        i -= 1
        j += 1
    if ln[0] == 0:
        ln[0] = 1
        ln.append(1)
    for x in ln:
        print(x, end="")
    print()
t -= 1
