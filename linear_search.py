def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__=="__main__":
    print(linear_search([5, 3, 7, 1, 4], 1))
    print(linear_search([5, 3, 7, 1, 4], 6))
    print(linear_search([1, 2, 2, 3], 2))
    print(linear_search([], 1))