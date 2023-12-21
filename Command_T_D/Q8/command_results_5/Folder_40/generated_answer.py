def all_even_ints_exclusive(nums):
    evens = []
    for i in range(0, 2):
        if i * 2 in nums:
            evens.append(i * 2)
    return evens
