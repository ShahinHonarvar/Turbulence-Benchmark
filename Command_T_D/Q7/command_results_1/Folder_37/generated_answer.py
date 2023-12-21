
def all_even_ints_inclusive(nums):
    evens = [i for i in range(1, len(nums) + 1) if not nums[i % 2]]
    return evens
