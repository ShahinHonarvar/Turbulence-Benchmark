
def sum_even_ints_inclusive(my_list):
    total = 0
    for i in range(30, 201, 2):
        if i < len(my_list):
            total += my_list[i]
    return total
