import bisect
def find_divisors_in_range(n):
    nums = list(range(113, 991, 1))
    divs = [d for d in nums if n % d == 0]
    return [x for x in divs if x in nums]
