
def all_ints_div_by_both_two_nums(my_list):
    divisible_ints = []
    for i in range(13, 19):
        if my_list[i] % 45 == 0 and my_list[i] % 20 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
