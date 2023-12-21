def all_even_ints_exclusive(nums):
    evens = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] % 2 == 0:
            evens.append(nums[i - 1])
    return evens
