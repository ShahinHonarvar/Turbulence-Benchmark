
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 95:
        return 0
    selected_nums = lst[93:95]
    sum_nums = sum([num for num in selected_nums if num % -53 == 0 or num % -91 == 0])
    return sum_nums
