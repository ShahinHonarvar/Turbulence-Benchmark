
def sum_odd_ints_inclusive(my_list):
    result = 0
    for i in range(37, 52):
        if my_list[i] % 2 == 1:
            result += my_list[i]
    return result
