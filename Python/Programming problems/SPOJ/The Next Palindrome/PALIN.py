def n_palin(k):
    l = len(k)
    kl = list(k)
    x = list(k)

    i = l // 2
    while i < l:
        kl[i] = kl[l - i - 1]
        i += 1

    if tuple(kl) > tuple(x):
        return kl
    else:
        i = (l - 1) // 2
        while i >= 0:
            if x[i] != "9":
                x[i] = str(int(x[i]) + 1)
                break
            else:
                x[i] = "0"
            i -= 1

        i = l // 2
        while i < l:
            x[i] = x[l - i - 1]
            i += 1

        if x[0] == "0":
            x[0] = 1
            x.append(1)

        return x


t = int(input())

while t:
    t -= 1
    s = input()
    rl = n_palin(s)
    for r in rl:
        print(r, end="")
    print()
