
def all_neg_ints_exclusive(int_list):
    negative_ints = []
    for i in range(69, 99):
        if i < len(int_list) and int_list[i] < 0:
            negative_ints.append(int_list[i])
    return negative_ints
