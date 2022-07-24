from math import floor


def binary_search(A, p, r, x):
    if p == r:
        if A[p] == x:
            return p
        else:
            return -1
    q = floor((p + r) / 2)
    if x <= A[q]:
        return binary_search(A, p, q, x)
    else:
        return binary_search(A, q + 1, r, x)


A = [-11111, 42, 9, 17, 54, 602, -3, 54, 999, -11]
A.sort()
print(A)
print(binary_search(A, 1, 9, 54))
print(binary_search(A, 1, 9, 53))
