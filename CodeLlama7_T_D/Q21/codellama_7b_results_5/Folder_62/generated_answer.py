
def all_ints_div_by_num(my_list):
    divisible_integers = []
    for i in range(87, 91):
        if my_list[i] % 55 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
