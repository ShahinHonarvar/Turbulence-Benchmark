
def sum_ints_div_by_either_nums(integers):
    sub_list = integers[44:60]
    return sum(num for num in sub_list if num % 39 == 0 or num % 15 == 0)
