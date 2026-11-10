def quirky_numbers(k):
    limit = 10 ** (2 * k)
    result = []
    s = 0
    while s * s < limit:
        n = s * s
        left = n // (10 ** k)
        right = n % (10 ** k)
        if left + right == s:
            result.append(n)
        s += 1
    return result