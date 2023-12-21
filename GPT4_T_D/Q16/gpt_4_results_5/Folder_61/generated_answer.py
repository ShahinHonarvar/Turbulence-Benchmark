
def sum_even_ints_inclusive(list_of_ints):
    sum_of_evens = 0
    for i in range(min(8, len(list_of_ints))):
        if list_of_ints[i] % 2 == 0:
            sum_of_evens += list_of_ints[i]
    return sum_of_evens
