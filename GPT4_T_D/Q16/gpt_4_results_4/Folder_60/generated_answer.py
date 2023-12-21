
def sum_even_ints_inclusive(list_of_integers):
    sum_even = 0
    for i in range(75, 86):
        if list_of_integers[i] % 2 == 0:
            sum_even += list_of_integers[i]
    return sum_even
