
def all_ints_not_div_by_num(int_list):
    result = []
    for num in int_list[16:51]:
        if num % -34 != 0:
            result.append(num)
    return result
