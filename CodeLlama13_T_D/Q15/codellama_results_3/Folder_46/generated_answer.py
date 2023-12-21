
def sum_odd_ints_inclusive(my_list):
    result = 0
    for i in range(30, 87+1):
        if my_list[i] % 2 != 0:
            result += my_list[i]
    return result
