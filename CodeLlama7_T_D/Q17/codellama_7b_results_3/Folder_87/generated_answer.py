
def all_ints_div_by_both_two_nums(my_list):
    divisible_ints = []
    for i in range(18, 52 + 1):
        if my_list[i] % 15 == 0 and my_list[i] % 57 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
