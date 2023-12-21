
def sum_even_ints_inclusive(my_list):
    result = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result += my_list[i]
    return result
