
def all_ints_div_by_both_two_nums(my_list):
    divisible_ints = []
    for i in range(54, 80):
        if my_list[i] % 54 == 0 and my_list[i] % 28 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
