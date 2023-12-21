
def sum_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 7:
        return 0
    else:
        if list_of_integers[6] % 2 == 0:
            return list_of_integers[6]
        else:
            return 0
