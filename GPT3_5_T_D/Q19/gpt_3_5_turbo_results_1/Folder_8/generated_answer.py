
def all_ints_not_div_by_num(integer_list):
    result = []
    for num in integer_list[17:88]:
        if num % -75 != 0:
            result.append(num)
    return result
