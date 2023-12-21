
def all_ints_div_by_both_two_nums(num_list):
    divisible_ints = []
    for i in range(72, 94):
        if num_list[i] % 32 == 0 and num_list[i] % 44 == 0:
            divisible_ints.append(num_list[i])
    return divisible_ints
