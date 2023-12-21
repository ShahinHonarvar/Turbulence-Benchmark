
def all_ints_div_by_num(lst):
    result = []
    for num in lst[45:81]:
        if num % 39 == 0:
            result.append(num)
    return result
