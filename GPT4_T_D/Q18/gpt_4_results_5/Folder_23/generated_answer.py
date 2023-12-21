
def sum_ints_div_by_either_nums(lst):
    sublist = lst[69:98]
    sum_divisible = sum([i for i in sublist if i % -90 == 0 or i % -67 == 0])
    return sum_divisible if sum_divisible != None else 0
