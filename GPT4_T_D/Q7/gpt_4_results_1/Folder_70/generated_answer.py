
def all_even_ints_inclusive(lst):
    even_int = []
    for i in range(28, 33):
        if lst[i] % 2 == 0:
            even_int.append(lst[i])
    return even_int
