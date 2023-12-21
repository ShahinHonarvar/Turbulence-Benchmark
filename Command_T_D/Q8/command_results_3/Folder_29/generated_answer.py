def all_even_ints_exclusive(nums):
    evens = []
    for i in range(48, 76):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
    return evens
