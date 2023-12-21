def sum_even_ints_inclusive(nums):
    return sum(nums[70:84]) if len(nums) >= 84 and len(nums) >= 70 and all(int(n) % 2 == 0 for n in nums[70:84]) else 0
