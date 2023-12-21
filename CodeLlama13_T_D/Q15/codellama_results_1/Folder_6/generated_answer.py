
def sum_odd_ints_inclusive(my_list):
    result = 0
    for i in range(10, 67, 2):
        if i < len(my_list) and my_list[i] % 2 != 0:
            result += my_list[i]
    return result
