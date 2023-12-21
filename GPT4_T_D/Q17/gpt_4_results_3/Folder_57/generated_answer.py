
def all_ints_div_by_both_two_nums(num_list):
    divisible_nums = []
    for i in range(51, 77):
        if num_list[i] % -90 == 0 and num_list[i] % -59 == 0:
            divisible_nums.append(num_list[i])
    return divisible_nums
