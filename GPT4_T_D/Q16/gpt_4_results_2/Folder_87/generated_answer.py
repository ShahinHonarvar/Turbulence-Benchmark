
def sum_even_ints_inclusive(list_ints):
    even_sum = 0
    for i in range(36, 47):
        if i < len(list_ints) and list_ints[i] % 2 == 0:
            even_sum += list_ints[i]
    return even_sum
