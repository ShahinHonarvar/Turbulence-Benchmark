
def sum_even_ints_inclusive(my_list):
    total = 0
    for i in range(31, 35):
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
