
def all_ints_not_div_by_num(integer_list):
    result = []
    for i in range(44, 91):
        if integer_list[i] % -68 != 0:
            result.append(integer_list[i])
    return result
