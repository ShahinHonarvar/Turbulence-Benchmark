
def all_ints_div_by_both_two_nums(int_list):
    valid_nums = []
    for i in range(40, 201):
        if i < len(int_list) and int_list[i] % 21 == 0 and int_list[i] % 71 == 0:
            valid_nums.append(int_list[i])
    return valid_nums
