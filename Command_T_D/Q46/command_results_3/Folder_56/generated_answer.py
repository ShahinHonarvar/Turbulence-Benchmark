
import functools
import operator

f = functools.reduce(operator.gcd, (int(n) for n in range(1, int(1e9) + 1)))

def gcf_three_nums(nums):
    return functools.reduce(operator.gcd, (int(n) for n in nums[:3])))
