
def all_even_ints_exclusive(lst):
    even_ints = []
    for i in range(27, 34):
        if i % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
