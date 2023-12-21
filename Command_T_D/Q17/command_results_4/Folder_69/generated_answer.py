
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for i in range(61, 88):
        if num_list[i]%31 == 0 and num_list[i]%11 == 0:
            result.append(num_list[i])
    return result
