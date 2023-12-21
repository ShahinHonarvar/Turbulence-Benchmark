
def all_even_ints_inclusive(nums):
    return [i for i in range(0, min(len(nums), 6) + 1) if nums[i] % 2 == 0]
