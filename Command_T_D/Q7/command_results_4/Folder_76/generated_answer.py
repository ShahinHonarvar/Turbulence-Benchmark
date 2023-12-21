
def all_even_ints_inclusive(nums):
    evens = [i for i in range(686, 987, 2) if nums[i] % 2 == 0]
    return [nums[i] for i in evens]
