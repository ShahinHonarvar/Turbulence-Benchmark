
def all_neg_ints_exclusive(int_list):
    result_list = []
    for i in range(1, len(int_list)-1):
        if int_list[i] < 0:
            result_list.append(int_list[i])
    return result_list
