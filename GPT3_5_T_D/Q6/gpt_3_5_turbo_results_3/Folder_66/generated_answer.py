
def all_neg_ints_exclusive(integer_list):
    negative_ints = []
    for i in range(13, 76):
        if integer_list[i] < 0:
            negative_ints.append(integer_list[i])
    return negative_ints
