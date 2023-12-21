
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = []
    for i in range(54, 80):
        if i < len(int_list) and int_list[i] % 54 == 0 and int_list[i] % 28 == 0:
            divisible_nums.append(int_list[i])
    return divisible_nums
