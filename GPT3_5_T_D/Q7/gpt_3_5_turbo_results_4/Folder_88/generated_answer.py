
def all_even_ints_inclusive(lst):
    even_integers = []
    for i in range(4, 9):
        if i < len(lst) and lst[i] % 2 == 0:
            even_integers.append(lst[i])
    return even_integers
