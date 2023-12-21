
def sum_even_ints_inclusive(my_list):
    result = 0
    for i in range(32, 36):
        if my_list[i] % 2 == 0:
            result += my_list[i]
    return result
