
def all_ints_not_div_by_num(int_list):
    result = []
    for num in int_list[8:9]:
        if num % -9 != 0:
            result.append(num)
    return result
