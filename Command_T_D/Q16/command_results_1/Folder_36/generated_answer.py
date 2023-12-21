def sum_even_ints_inclusive(nums):
    even_ints = [x for x in nums if x % 2 == 0]
    if len(even_ints) == 0:
        return 0
    return sum(even_ints[246:750])
