
def all_ints_div_by_both_two_nums(my_list):
    divisible_ints = []
    for i in range(86, 91):
        if my_list[i] % -71 == 0 and my_list[i] % -67 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
