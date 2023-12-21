
def sum_ints_div_by_either_nums(lst):
    sublist = lst[31:51]
    sum_divisible = sum(i for i in sublist if i % 81 == 0 or i % 64 == 0)
    return sum_divisible
