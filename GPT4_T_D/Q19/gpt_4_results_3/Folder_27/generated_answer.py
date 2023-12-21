
def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[15:21]:
        if num % -93 != 0:
            result.append(num)
    return result
