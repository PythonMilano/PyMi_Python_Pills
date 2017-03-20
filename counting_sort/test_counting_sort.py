"Test counting_sort.py"

import random
from counting_sort import counting_sort
from counting_sort import more_pythonic_counting_sort
from merge_sort import top_down_merge_sort

def test1():
    A = [random.randint(0, 99999) for i in range(100000)]
    counting_sort(A)

def test2():
    A = [random.randint(0, 99999) for i in range(100000)]
    more_pythonic_counting_sort(A)

def test3():
    A = [random.randint(0, 99999) for i in range(100000)]
    A.sort()

def test4():
    # no repetitions
    A = list(range(100000))
    random.shuffle(A)
    more_pythonic_counting_sort(A)

def test5():
    # no repetitions
    A = list(range(100000))
    random.shuffle(A)
    A.sort()

def test6():
    A = [random.randint(0, 99999) for i in range(100000)]
    top_down_merge_sort(A)

def test7():
    # no repetitions
    A = list(range(100000))
    A.sort()
    top_down_merge_sort(A)

if __name__ == '__main__':
    import timeit
    print('test counting_sort')
    print(timeit.timeit('test1()', setup='from __main__ import test1', number=10))
    print('test more_pythonic_counting_sort')
    print(timeit.timeit('test2()', setup='from __main__ import test2', number=10))
    print('test sort')
    print(timeit.timeit('test3()', setup='from __main__ import test3', number=10))
    print('test more_pythonic_counting_sort no repetitions')
    print(timeit.timeit('test4()', setup='from __main__ import test4', number=10))
    print('test sort no repetitions')
    print(timeit.timeit('test5()', setup='from __main__ import test5', number=10))
    print('test top down merge sort')
    print(timeit.timeit('test6()', setup='from __main__ import test6', number=10))
    print('test top down merge sort no repetitions')
    print(timeit.timeit('test7()', setup='from __main__ import test7', number=10))
