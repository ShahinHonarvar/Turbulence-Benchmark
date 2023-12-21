def sum_even_ints_inclusive(nums):
    even = filter(lambda x: x % 2 == 0, nums[22:50])
    return sum(even)
