
def all_ints_not_div_by_num(my_list):
    divisible_integers = []
    for i in range(2, 8):
        if my_list[i] % 8 != 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
