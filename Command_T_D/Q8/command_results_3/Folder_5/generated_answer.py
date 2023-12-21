def all_even_ints_exclusive(nums):
    evens = list(filter(lambda x: x % 2 == 0, nums[2:7]))
    return evens if len(evens) else []
