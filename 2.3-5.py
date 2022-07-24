def insertion_sort(A, n):
    if 1 == n:
        return A
    A = insertion_sort(A, n - 1)
    big_index = n - 1
    new_value = A[n]
    while new_value < A[big_index] and big_index > 0:
        A[big_index + 1] = A[big_index]
        big_index = big_index - 1
    A[big_index + 1] = new_value
    return A


# must overallocate array and not use 0th element
# tests from https://reprog.wordpress.com/2010/05/20/what-does-it-take-to-test-a-sorting-routine/
print(insertion_sort([11111, 42, 9, 17, 54, 602, -3, 54, 999, -11], 9))
print(insertion_sort([11111, 42, 9, 17, 54, 602, -3, 54, 999, -11, -1111], 10))
