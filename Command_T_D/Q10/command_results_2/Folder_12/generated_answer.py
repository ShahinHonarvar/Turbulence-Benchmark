def all_odd_ints_exclusive(nums):
    odd = [n for n in range(23, 45) if n % 2 == 1]
    return [n for n in nums if n in odd]
