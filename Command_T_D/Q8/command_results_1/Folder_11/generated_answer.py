def all_even_ints_exclusive(nums):
    even_ints = []
    for i in range(15, 99):
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints
