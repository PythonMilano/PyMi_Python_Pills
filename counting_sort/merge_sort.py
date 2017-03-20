"""Top down Merge Sort implementation."""


def top_down_merge_sort(A):
    if len(A) > 1:
        # splitting phase
        mid = len(A) // 2
        left = A[:mid]
        rigth = A[mid:]

        top_down_merge_sort(left)
        top_down_merge_sort(rigth)

        # merge phase
        i=0
        j=0
        k=0
        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                A[k]=left[i]
                i=i+1
            else:
                A[k]=rigth[j]
                j=j+1
            k=k+1

        while i < len(left):
            A[k]=left[i]
            i=i+1
            k=k+1

        while j < len(rigth):
            A[k]=rigth[j]
            j=j+1
            k=k+1


if __name__ == '__main__':
    # basic unit tests
    A = [3,2,5,6,3,8,9,11]
    top_down_merge_sort(A)
    assert A == [2,3,3,5,6,8,9,11]
    A = [11,2]
    top_down_merge_sort(A)
    assert A == [2,11]
    A = [2]
    top_down_merge_sort(A)
    assert A == [2]
    A = [-1,-2,3,0]
    top_down_merge_sort(A)
    assert A == [-2,-1,0,3]
