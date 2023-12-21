
def all_ints_div_by_num(lst):
    result = []
    for num in lst[1:5]:
        if num % -6 == 0:
            result.append(num)
    return result
