
def sum_ints_div_by_either_nums(lst):
    filtered_list = [i for i in lst[38:53] if i % -41 == 0 or i % -47 == 0]
    return sum(filtered_list) if filtered_list else 0
