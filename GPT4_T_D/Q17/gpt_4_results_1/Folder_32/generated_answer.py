
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(25, 96):
        if int_list[i] % 51 == 0 and int_list[i] % 77 == 0:
            result.append(int_list[i])
    return result
