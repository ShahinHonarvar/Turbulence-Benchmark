
def all_ints_div_by_both_two_nums(input_list):
    divisible_ints = []
    for i in range(25, 81):
        if input_list[i] % -20 == 0 and input_list[i] % -26 == 0:
            divisible_ints.append(input_list[i])
    return divisible_ints
