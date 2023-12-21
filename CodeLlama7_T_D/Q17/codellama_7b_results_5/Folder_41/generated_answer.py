
def all_ints_div_by_both_two_nums(my_list):
    divisible_integers = []
    for i in range(len(my_list)):
        if my_list[i] % 6 == 0 and my_list[i] % (-3) == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
