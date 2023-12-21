
def all_neg_ints_exclusive(int_list):
    neg_nums = []
    for i in range(39, 81):
        if i < len(int_list) and int_list[i] < 0:
            neg_nums.append(int_list[i])
    return neg_nums
