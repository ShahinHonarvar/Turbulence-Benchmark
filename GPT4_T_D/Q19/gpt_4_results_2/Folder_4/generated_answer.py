
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(20, 49):
        if i<len(int_list) and int_list[i] % -36 !=0:
            result.append(int_list[i])
    return result
