
def all_ints_div_by_num(int_list):
    divisible_list = []
    for i in range(14, 69):
        if int_list[i] % 18 == 0:
            divisible_list.append(int_list[i])
    return divisible_list
