
def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[10:80]:
        if num % -74 == 0 and num % -58 == 0:
            result.append(num)
    return result
