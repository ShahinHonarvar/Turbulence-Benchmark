
def all_ints_div_by_num(my_list):
    divisible_integers = []
    for i in range(59, 79 + 1):
        if my_list[i] % -82 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
