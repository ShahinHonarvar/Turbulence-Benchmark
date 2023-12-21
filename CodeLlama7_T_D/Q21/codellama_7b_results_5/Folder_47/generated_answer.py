
def all_ints_div_by_num(my_list):
    result = []
    for i in range(75, 89):
        if my_list[i] % -27 == 0:
            result.append(my_list[i])
    return result
