
def sum_ints_div_by_either_nums(lst):
    subset = lst[:2]
    sum_num = sum([num for num in subset if num % 1 == 0 or num % 2 == 0])
    return sum_num
