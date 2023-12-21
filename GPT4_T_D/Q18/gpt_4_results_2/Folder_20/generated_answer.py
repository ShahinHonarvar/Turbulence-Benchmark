
def sum_ints_div_by_either_nums(lst):
    relevant_nums = lst[48:77]
    return sum(num for num in relevant_nums if num % -46 == 0 or num % -82 == 0)
