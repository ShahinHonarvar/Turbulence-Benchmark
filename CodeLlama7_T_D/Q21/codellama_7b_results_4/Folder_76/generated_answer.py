
def all_ints_div_by_num(my_list):
    result = []
    for i in range(601, 698 + 1):
        if my_list[i] % 901 == 0:
            result.append(my_list[i])
    return result
