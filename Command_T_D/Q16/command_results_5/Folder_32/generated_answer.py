def sum_even_ints_inclusive(nums):
    even_ints = [x for x in range(21, 97, 2) if x in nums]
    return sum(even_ints) if even_ints else 0
