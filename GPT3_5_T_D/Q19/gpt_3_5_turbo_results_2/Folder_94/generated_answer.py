
def all_ints_not_div_by_num(integers):
    result = []
    for num in integers[24:45]:
        if num % -72 != 0:
            result.append(num)
    return result
