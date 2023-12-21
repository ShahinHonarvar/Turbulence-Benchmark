
def sum_even_ints_inclusive(list_of_ints):
    even_sum = 0
    for i in range(64, 67):
        if i < len(list_of_ints) and list_of_ints[i] % 2 == 0:
            even_sum += list_of_ints[i]
    return even_sum
