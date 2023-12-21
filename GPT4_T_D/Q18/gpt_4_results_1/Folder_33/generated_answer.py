
def sum_ints_div_by_either_nums(lst):
    lst = lst[281:695]
    sum_num = sum(num for num in lst if num % -722 == 0 or num % -731 == 0)
    return sum_num if sum_num else 0
