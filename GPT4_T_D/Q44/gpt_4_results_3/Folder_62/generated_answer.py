
import math 

def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(30, min(88, len(lst))):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums
