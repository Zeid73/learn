def closestPalindrome(n):
    # Initialize a list to store the candidate palindromic numbers
    candidates = []

    # Get the length of the input number n
    length = len(n)

    # Calculate the index of the middle element (or the element just after the middle for even-length numbers)
    mid = (length + 1) // 2

    # If the input number has only one digit, the closest palindromic number is (n-1)
    if length == 1:
        return str(int(n) + 1)

    # Add two candidates: (10^n + 1) and (10^(n-1) - 1)
    candidates.append(10**length + 1)
    # candidates.append(10 ** (length - 1) - 1)

    # Extract the prefix (first half) of the input number
    prefix = int(n[:mid])

    # Generate three possible prefixes by incrementing and decrementing the original prefix
    temp = [prefix, prefix + 1]
    # Construct the candidate palindromic numbers using the generated prefixes
    for i in temp:
        res = str(i)
        # If the length of the input number is odd, exclude the last character while constructing the palindromic number
        if length & 1:
            res = res[:-1]
        # Create the palindromic number by appending the reverse of the prefix
        peep = str(i) + res[::-1]
        candidates.append(int(peep))

    # Initialize variables to keep track of the minimum difference and the closest palindromic number
    minDiff = float("inf")
    result = tip = int(n)

    # Iterate through the candidate palindromic numbers and find the closest one to the input number
    for i in range(3):
        if (
            candidates[i] > int(n)
            and candidates[i] != tip
            and minDiff > abs(candidates[i] - tip)
        ):
            result = candidates[i]
            minDiff = abs(candidates[i] - tip)
        # If there are multiple candidates with the same difference, choose the smaller one
        elif abs(candidates[i] - tip) == minDiff:
            result = max(result, candidates[i])

    return str(result)


# driver's code
t = int(input())

while t:
    t -= 1
    s = input()
    print(closestPalindrome(s))
