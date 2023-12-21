def all_even_ints_exclusive(nums):
    evens = []
    for i in range(25, 81):
        if i % 2 == 0:
            evens.append(i)
    return evens
