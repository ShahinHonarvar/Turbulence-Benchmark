def sum_even_ints_inclusive(nums):
    even_nums = filter(lambda x: x % 2 == 0, nums[22:63])
    return sum(even_nums) if even_nums else 0
