
def all_ints_div_by_both_two_nums(int_lst):
    divisible_nums = []
    for i in int_lst[38:53]:
        if i % -41 == 0 and i % -47 == 0:
            divisible_nums.append(i)
    return divisible_nums
