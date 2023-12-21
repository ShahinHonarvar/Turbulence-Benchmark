def all_even_ints_exclusive(lst):
    even = []
    for i in range(20, 93):
        if i % 2 == 0:
            even.append(i)
    return even
