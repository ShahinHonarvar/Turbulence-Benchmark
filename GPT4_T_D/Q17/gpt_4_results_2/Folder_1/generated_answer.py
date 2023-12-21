
def all_ints_div_by_both_two_nums(int_list):
    divisible_list = []
    for i in range(10, 29):
        if int_list[i] % -61 == 0 and int_list[i] % -64 == 0:
            divisible_list.append(int_list[i])
    return divisible_list
