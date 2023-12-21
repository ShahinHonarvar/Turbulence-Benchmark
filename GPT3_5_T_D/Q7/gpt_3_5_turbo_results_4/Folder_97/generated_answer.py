
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(40, 81):
        if i < len(lst) and lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
