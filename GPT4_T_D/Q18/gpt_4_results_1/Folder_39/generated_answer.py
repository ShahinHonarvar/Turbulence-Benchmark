
def sum_ints_div_by_either_nums(lst):
    lst_slice = lst[13:77]
    sum_nums = sum(num for num in lst_slice if num % -66 == 0 or num % -32 == 0)
    return sum_nums
