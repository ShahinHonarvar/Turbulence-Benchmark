def all_even_ints_exclusive(nums):
    evens = [e for e in nums[20:200] if e % 2 == 0]
    return evens if evens else []
