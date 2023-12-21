def all_even_ints_exclusive(nums):
    evens = [x for x in range(2, len(nums) + 1, 2) if nums[x - 2] % 2 == 0]
    return evens[1:4]
