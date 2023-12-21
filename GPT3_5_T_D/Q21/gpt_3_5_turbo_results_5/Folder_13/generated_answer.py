
def all_ints_div_by_num(int_list):
    divisible_list = []
    for i in range(36, 41):
        if int_list[i] % 28 == 0:
            divisible_list.append(int_list[i])
    return divisible_list
