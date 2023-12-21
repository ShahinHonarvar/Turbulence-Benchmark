def all_even_ints_exclusive(nums):
    evens = [i for i in range(3, 8) if i % 2 == 0]
    return [nums[e] for e in evens] if evens else []
