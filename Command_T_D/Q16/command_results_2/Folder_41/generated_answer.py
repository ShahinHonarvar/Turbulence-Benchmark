def sum_even_ints_inclusive(nums):
    return sum(nums[6:6] if even(nums[6:6]) else 0)
def even(nums):
    return all(int(nums[0]) % 2 == int(nums[1]) % 2 for i in range(len(nums) - 1))
