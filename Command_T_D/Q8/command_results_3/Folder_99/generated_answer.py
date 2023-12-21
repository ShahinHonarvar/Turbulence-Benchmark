def all_even_ints_exclusive(nums):
    evens = []
    for i in range(295, 573, 2):
        if i in nums:
            evens.append(i)
    return evens
