
def all_ints_div_by_both_two_nums(lst):
    div_nums = []
    for i in range(20, 94):
        if lst[i] % -92 == 0 and lst[i] % -50 == 0:
            div_nums.append(lst[i])
    return div_nums
