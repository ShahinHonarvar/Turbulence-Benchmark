
def sum_odd_ints_inclusive(my_list):
    result = 0
    for i in range(70, 201, 2):
        if my_list[i]:
            result += my_list[i]
    return result
