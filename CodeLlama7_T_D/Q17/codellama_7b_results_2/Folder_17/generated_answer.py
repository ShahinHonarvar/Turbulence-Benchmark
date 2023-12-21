
def all_ints_div_by_both_two_nums(my_list):
    divisible_integers = []
    for i in range(81, 90):
        if my_list[i] % 56 == 0 and my_list[i] % 68 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
