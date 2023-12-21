import math
def composite_nums_between_indices(nums):
    c = set()
    for i in range(6, 7):
        if i in nums:
            c.add(i)
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    c.add(i // j)
                    break
    return c
