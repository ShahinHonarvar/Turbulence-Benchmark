
def all_ints_div_by_num(my_list):
    divisible_integers = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
