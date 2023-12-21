
def sum_odd_ints_inclusive(list_of_integers):
    odd_sum = 0
    for i in range(1, min(9, len(list_of_integers))): 
        if list_of_integers[i] % 2 != 0:
            odd_sum += list_of_integers[i]
    return odd_sum
