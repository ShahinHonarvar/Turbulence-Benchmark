
def all_ints_div_by_both_two_nums(int_lst):
    valid_nums = []
    for num in int_lst[58:82]:
        if num % 55 == 0 and num % 10 == 0:
            valid_nums.append(num)
    return valid_nums
