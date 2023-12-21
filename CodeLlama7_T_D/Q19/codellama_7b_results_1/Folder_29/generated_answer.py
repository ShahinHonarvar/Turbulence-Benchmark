
def all_ints_not_div_by_num(my_list):
    divisible_integers = []
    for i in range(24, 25):
        if my_list[i] % -30 != 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
