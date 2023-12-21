
def all_ints_div_by_both_two_nums(lst):
    div_nums = []
    for i in range(34, 70):
        if lst[i] % 19 == 0 and lst[i] % 32 == 0:
            div_nums.append(lst[i])
    return div_nums
