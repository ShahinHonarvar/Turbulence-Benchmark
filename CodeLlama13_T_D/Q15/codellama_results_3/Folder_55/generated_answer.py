
def sum_odd_ints_inclusive(my_list):
    result = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0 and i >= 0 and i <= 10:
            result += my_list[i]
    return result
