
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(240, 901):
        if my_list[i] % 546 == 0 or my_list[i] % 709 == 0:
            result += my_list[i]
    return result
