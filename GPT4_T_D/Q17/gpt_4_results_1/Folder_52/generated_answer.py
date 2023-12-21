
def all_ints_div_by_both_two_nums(int_list):
    valid_nums = []
    for i in range(48, 60):
        if i < len(int_list):
            if int_list[i] % 88 == 0 and int_list[i] % 58 == 0:
                valid_nums.append(int_list[i])
    return valid_nums
