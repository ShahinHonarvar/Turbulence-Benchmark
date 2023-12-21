
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for i in range(8, 9):
        if num_list[i] % 3 == 0 and num_list[i] % 6 == 0:
            result.append(num_list[i])
    return result
