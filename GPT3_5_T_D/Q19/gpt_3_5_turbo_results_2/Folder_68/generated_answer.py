
def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[:7]:
        if num % 7 != 0:
            result.append(num)
    return result
