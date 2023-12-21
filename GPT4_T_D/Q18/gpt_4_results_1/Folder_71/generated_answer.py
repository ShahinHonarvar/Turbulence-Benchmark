
def sum_ints_div_by_either_nums(list_ints):
    target_ints = list_ints[68:100]
    target_sum = sum(x for x in target_ints if x % -37 == 0 or x % -26 == 0)
    return target_sum
