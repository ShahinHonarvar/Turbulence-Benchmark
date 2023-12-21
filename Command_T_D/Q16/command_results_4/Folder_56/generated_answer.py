def sum_even_ints_inclusive(nums):
    even = [x for x in nums if x % 2 == 0]
    if len(even) > 0:
        return sum(even)
    else:
        return 0
