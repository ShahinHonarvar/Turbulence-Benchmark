
def sum_even_ints_inclusive(list_of_integers):
    return sum(num for i, num in enumerate(list_of_integers[8:81]) if num % 2 == 0)
