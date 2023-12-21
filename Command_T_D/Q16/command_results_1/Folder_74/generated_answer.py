def sum_even_ints_inclusive(nums):
    even_ints = [nums[i] for i in range(17,79) if nums[i] % 2 == 0]
    return sum(even_ints) if even_ints else 0
