def sum_even_ints_inclusive(nums):
    even = next((el for el in nums if el % 2 == 0), None)
    return even if even is not None else 0
