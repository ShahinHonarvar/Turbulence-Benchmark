
def all_even_ints_inclusive(nums):
    return [i for i in range(1, len(nums) + 1) if not nums[i - 1] % 2]
