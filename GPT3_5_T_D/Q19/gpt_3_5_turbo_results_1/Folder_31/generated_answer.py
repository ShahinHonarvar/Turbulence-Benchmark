
def all_ints_not_div_by_num(int_list):
    result = []
    for num in int_list[18:37]:
        if num % -67 != 0:
            result.append(num)
    return result
