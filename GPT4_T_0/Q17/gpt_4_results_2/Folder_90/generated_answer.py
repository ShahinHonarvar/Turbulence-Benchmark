
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = []
    for i in range(138, 425):
        if int_list[i] % -863 == 0 and int_list[i] % -329 == 0:
            divisible_nums.append(int_list[i])
    return divisible_nums
