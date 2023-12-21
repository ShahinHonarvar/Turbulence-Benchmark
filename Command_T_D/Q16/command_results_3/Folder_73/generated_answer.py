def sum_even_ints_inclusive(nums):
    even = [i for i in range(19, 93, 2) if i in nums]
    return sum(even) if even else 0
