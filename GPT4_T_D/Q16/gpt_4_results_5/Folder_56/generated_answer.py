
def sum_even_ints_inclusive(lst):
    if lst == []:
        return 0
    elif lst[0] % 2 == 0:
        return lst[0]
    else:
        return 0
