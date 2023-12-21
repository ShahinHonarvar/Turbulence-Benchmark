
def all_ints_div_by_both_two_nums(lst):
    div_nums = []
    for i in range(38, 53):
        if lst[i] % -41 == 0 and lst[i] % -47 == 0:
            div_nums.append(lst[i])
    return div_nums
