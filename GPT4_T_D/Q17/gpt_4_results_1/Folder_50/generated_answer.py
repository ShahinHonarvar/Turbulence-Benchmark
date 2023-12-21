
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(46, 92):
        if i < len(int_list) and int_list[i] % 67 == 0 and int_list[i] % 15 == 0:
            result.append(int_list[i])
    return result
