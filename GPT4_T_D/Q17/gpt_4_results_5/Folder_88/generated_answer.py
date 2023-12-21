
def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    for i in range(3, 10):
        if int_list[i] % 6 == 0 and int_list[i] % 1 == 0:
            divisible_ints.append(int_list[i])
    return divisible_ints
