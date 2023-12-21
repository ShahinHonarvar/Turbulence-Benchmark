
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = []
    for i in range(154, 799):
        if int_list[i] % 275 == 0 and int_list[i] % 580 == 0:
            divisible_nums.append(int_list[i])
    return divisible_nums
