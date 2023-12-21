
def all_ints_div_by_num(int_list):
    divisible_ints = []
    for i in range(44, 74):
        if int_list[i] % 88 == 0:
            divisible_ints.append(int_list[i])
    return divisible_ints
