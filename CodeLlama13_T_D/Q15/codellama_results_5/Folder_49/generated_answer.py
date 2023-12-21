
def sum_odd_ints_inclusive(my_list):
    result = 0
    for i in range(80, 201, 2):
        if i in my_list:
            result += my_list[i]
    return result
