
def all_ints_div_by_num(int_list):
    divisible_ints = []
    for i in range(27, 91):
        if int_list[i] % 57 == 0:
            divisible_ints.append(int_list[i])
    return divisible_ints
