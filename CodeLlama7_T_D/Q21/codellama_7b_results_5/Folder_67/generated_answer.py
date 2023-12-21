
def all_ints_div_by_num(my_list):
    divisible_integers = []
    for i in range(40, 68 + 1):
        if my_list[i] % 16 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
