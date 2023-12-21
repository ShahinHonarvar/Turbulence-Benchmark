
def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[1:9]:
        if num % -9 == 0 or num % -3 == 0:
            result += num
    return result
