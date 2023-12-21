def all_even_ints_exclusive(nums):
    evens = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return evens if evens else []
