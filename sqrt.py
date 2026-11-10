def integer_square_root(n):
    left = 0
    right = n
    answer = 0
    while left <= right:
        middle = (left + right) // 2
        if middle * middle <= n:
            answer = middle
            left = middle + 1
        else:
            right = middle - 1
    return answer