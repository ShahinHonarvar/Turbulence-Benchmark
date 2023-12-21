
def all_ints_div_by_both_two_nums(num_list):
    divisible_nums = []
    for i in range(29, 54):
        if num_list[i] % -68 == 0 and num_list[i] % -85 == 0:
            divisible_nums.append(num_list[i])
    return divisible_nums
