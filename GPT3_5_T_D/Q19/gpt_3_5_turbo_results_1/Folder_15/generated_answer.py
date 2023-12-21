
def all_ints_not_div_by_num(integer_list):
    result = []
    for num in integer_list[:2]:
        if num % -2 != 0:
            result.append(num)
    return result
