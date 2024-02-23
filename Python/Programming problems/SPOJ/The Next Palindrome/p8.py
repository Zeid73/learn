def findNextPalin(k):
    lk = len(k)
    x = k
    K = list(k)
    for i in range(lk // 2, lk):
        K[i] = K[lk - i - 1]
    if K > x:
        return K
    else:
        for i in range((lk - 1) // 2, -1, -1):
            if x[i] != "9":
                x[i] += 1
                break
            else:
                x[i] = "0"
        for i in range(lk // 2, lk):
            x[i] = x[lk - i - 1]
        if x[0] == "0":
            x += "1"
            x[0] = "1"
        return x


T = int(input())
while T > 0:
    K = input()
    print(findNextPalin(K))
    T -= 1
