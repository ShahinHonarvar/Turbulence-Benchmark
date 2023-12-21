
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(61, 89):
        if my_list[i] % 31 == 0 and my_list[i] % 11 == 0:
            result.append(my_list[i])
    return result
