
def all_ints_not_div_by_num(num_list):
    result = []
    for i in num_list[1:2]:
        if i % -2 != 0:
            result.append(i)
    return result
