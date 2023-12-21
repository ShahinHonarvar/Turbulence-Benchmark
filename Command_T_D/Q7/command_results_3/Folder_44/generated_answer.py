
def all_even_ints_inclusive(nums):
    evens = [nums[i] for i in range(13, 68) if nums[i] % 2 == 0]
    return evens if len(evens) > 0 else []
