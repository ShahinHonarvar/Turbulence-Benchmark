
def all_even_ints_inclusive(lst):
    evens = []
    for i in range(75, 86):
        if i < len(lst) and lst[i] % 2 == 0:
            evens.append(lst[i])
    return evens
