def all_even_ints_exclusive(nums):
    evens = []
    for i in range(10, len(nums) + 10):
        if i % 2 == 0:
            evens.append(nums[i - 1])
    return evens
