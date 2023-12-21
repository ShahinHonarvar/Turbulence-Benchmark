def sum_even_ints_inclusive(nums):
    even = [i for i in range(len(nums) - 1, -1, -1) if nums[i] % 2 == 0]
    return sum(nums[i] for i in even if i >= 62 and i <= 99)
