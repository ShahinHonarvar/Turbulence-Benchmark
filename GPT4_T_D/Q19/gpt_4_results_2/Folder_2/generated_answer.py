
def all_ints_not_div_by_num(int_list):
    result_list = []
    for num in int_list[21:50]:
        if num % 40 != 0:
            result_list.append(num)
    return result_list
