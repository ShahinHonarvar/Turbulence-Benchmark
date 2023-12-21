
def all_ints_div_by_num(my_list):
    divisible_ints = []
    for i in range(29, 51 + 1):
        if my_list[i] % -37 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
