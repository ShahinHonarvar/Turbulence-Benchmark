
def sum_ints_div_by_either_nums(lst):
    index_range = lst[55:81]
    result = sum(i for i in index_range if i % 22 == 0 or i % 32 == 0)
    return result
