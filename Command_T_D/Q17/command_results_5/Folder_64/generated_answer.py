
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for i in range(len(num_list)):
        if num_list[i] % 11 == 0 and num_list[i] % -7 == 0:
            result.append(num_list[i])
    return result
