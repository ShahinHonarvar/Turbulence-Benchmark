
def all_even_ints_inclusive(nums):
    return [n for n in nums if n % 2 == 0 and 0 <= n <= 0] or []
