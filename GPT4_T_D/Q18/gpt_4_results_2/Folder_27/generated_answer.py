
def sum_ints_div_by_either_nums(lst):
    selected_ints = lst[20:36]
    sum_num = sum([num for num in selected_ints if num % -36 == 0 or num % -89 == 0])
    return sum_num
