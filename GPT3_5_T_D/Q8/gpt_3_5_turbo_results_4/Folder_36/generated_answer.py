
def all_even_ints_exclusive(lst):
    evens = []
    for i in range(598, 767):
        if i % 2 == 0:
            evens.append(lst[i])
    return evens
