def find_even_index(numbers):
    total = sum(numbers)
    left_sum = 0
    for i in range(len(numbers)):
        right_sum = total - left_sum - numbers[i]
        if left_sum == right_sum:
            return i
        left_sum += numbers[i]
    return -1