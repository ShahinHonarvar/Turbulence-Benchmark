
def all_ints_not_div_by_num(my_list):
    divisible_ints = []
    for i in range(38, 52):
        if my_list[i] % -41 != 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
