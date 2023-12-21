
def all_ints_div_by_both_two_nums(int_list):
    result_list = []
    for i in range(29, 46):
        try:
            if int_list[i] % 27 == 0 and int_list[i] % 81 == 0:
                result_list.append(int_list[i])
        except IndexError:
            break
    return result_list
