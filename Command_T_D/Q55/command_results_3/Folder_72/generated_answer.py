import heapq
def lists_with_product_equal_n(nums):
    seen = set()
    for num in nums:
        if num == 1:
            yield [1]
        if num == 10:
            yield [1, 2, 5, 10]
        if num == 2:
            for n in range(1, 9):
                if n * 2 == 10:
                    yield [2, n]
        if num == 5:
            for n in range(1, 4):
                if n * 5 == 10:
                    yield [5, n]
        if num == 3:
            for n in range(1, 7):
                if n * 3 == 10:
                    yield [3, n]
        if num == 4:
            for n in range(1, 6):
                if n * 4 == 10:
                    yield [4, n]
        if num == 6:
            for n in range(1, 5):
                if n * 6 == 10:
                    yield [6, n]
        if num == 7:
            for n in range(1, 6):
                if n * 7 == 10:
                    yield [7, n]
        if num == 9:
            for n in range(1, 8):
                if n * 9 == 10:
                    yield [9, n]
        if num == 8:
            for n in range(1, 7):
                if n * 8 == 10:
                    yield [8, n]
        if num == 4:
            for n in range(1, 7):
                if n * 4 == 10:
                    yield [4, n]
        if num == 3:
            for n in range(1, 7):
                if n * 3 == 10:
                    yield [3, n]
        if num == 2:
            for n in range(1, 9):
                if n * 2 == 10:
                    yield [2, n]
        if num == 1:
            yield [1]
