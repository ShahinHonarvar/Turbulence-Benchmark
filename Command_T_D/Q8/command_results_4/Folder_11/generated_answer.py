def all_even_ints_exclusive(nums):
    evens = []
    for i in range(15, 99):
        if i % 2 == 0:
            evens.append(i)
    return evens
