def min_pair_sum(numbers):
    numbers = sorted(numbers)
    total = 0
    n = len(numbers)
    for i in range(n // 2):
        total += numbers[i] * numbers[n - 1 - i]
    return total