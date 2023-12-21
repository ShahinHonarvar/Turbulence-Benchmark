
def all_ints_not_div_by_num(integer_list):
    not_divisible_list = []
    for i in range(20, 35):
        if integer_list[i] % -36 != 0:
            not_divisible_list.append(integer_list[i])
    return not_divisible_list
