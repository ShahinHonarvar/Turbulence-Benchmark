
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for index in range(0, len(int_list)):
        if int_list[index] % 13 == 0 and int_list[index] % -1 == 0:
            result.append(int_list[index])
    return result
