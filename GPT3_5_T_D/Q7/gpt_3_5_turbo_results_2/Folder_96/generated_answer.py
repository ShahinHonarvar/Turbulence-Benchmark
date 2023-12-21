
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(50, 201):
        if i % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
