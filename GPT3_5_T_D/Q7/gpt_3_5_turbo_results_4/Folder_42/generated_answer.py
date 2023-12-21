
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(29, 80):
        if i % 2 == 0 and i < len(lst):
            even_ints.append(lst[i])
    return even_ints
