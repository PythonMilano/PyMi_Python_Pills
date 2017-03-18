"""Counting sort: O(N) for integer arrays."""

def counting_sort(A):
    "Sort the 'array' of int A."
    if len(A) <= 1:
        return A
    M = A[0]
    m = A[0]
    for i in range(1, len(A)):
        if A[i] > M:
            M = A[i]
        if A[i] < m:
            m = A[i]
    # frequency array of the range
    C = [0] * (M - m + 1)
    for i in range(len(A)):
        C[A[i] - m] = C[A[i] - m] + 1
    # construct sorted A from C
    k = 0
    for i in range(len(C)):
        while C[i] > 0:
            A[k] = m + i
            C[i] = C[i] - 1
            k = k + 1
    return A


def more_pythonic_counting_sort(A):
    "Sort the 'array' of int A."
    if len(A) <= 1:
        return A
    m = min(A)
    # frequency array of the range
    C = [0] * (max(A) - m + 1)
    for a in A:
        C[a - m] = C[a - m] + 1
    # construct sorted A from C
    k = 0
    for i in range(len(C)):
        while C[i] > 0:
            A[k] = m + i
            C[i] = C[i] - 1
            k = k + 1
    return A

if __name__ == '__main__':
    # basic unit tests
    A = [3,2,5,6,3,8,9,11]
    counting_sort(A)
    assert A == [2,3,3,5,6,8,9,11]
    A = [11,2]
    counting_sort(A)
    assert A == [2,11]
    A = [2]
    counting_sort(A)
    assert A == [2]
    A = [-1,-2,3,0]
    counting_sort(A)
    assert A == [-2,-1,0,3]
    A = [3,2,5,6,3,8,9,11]
    more_pythonic_counting_sort(A)
    assert A == [2,3,3,5,6,8,9,11]
    A = [11,2]
    more_pythonic_counting_sort(A)
    assert A == [2,11]
    A = [2]
    more_pythonic_counting_sort(A)
    assert A == [2]
    A = [-1,-2,3,0]
    more_pythonic_counting_sort(A)
    assert A == [-2,-1,0,3]
