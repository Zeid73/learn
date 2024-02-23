def next_pal(x):
    s = str(x)
    if len(s) % 2:  # odd
        # take the first half (including the middle digit)
        first_half = s[: len(s) // 2 + 1]
        # construct a number that's that half,
        # plus itself reversed (without the middle digit)
        candidate = int(first_half + first_half[-2::-1])
        # that number could be smaller (e.g. if we started with 245)
        if candidate > x:
            return candidate
        # let's try again: we increment the first half and do the same thing:
        new_first_half = str(int(first_half) + 1)
        # but be careful: we could be adding a digit here (e.g. 999 -> 100001)
        if len(new_first_half) == len(first_half):
            return int(new_first_half + new_first_half[-2::-1])
        # instead, in those cases, we just return the smallest palindrome of that length
        return 10 ** len(s) + 1
    else:  # even
        # similar dance for even
        first_half = s[: len(s) // 2]
        candidate = int(first_half + first_half[::-1])
        if candidate > x:
            return candidate
        new_first_half = str(int(first_half) + 1)
        if len(new_first_half) == len(first_half):
            return int(new_first_half + new_first_half[::-1])
        return 10 ** len(s) + 1


t = int(input())

while t:
    t -= 1
    s = input()
    print(next_pal(s))
