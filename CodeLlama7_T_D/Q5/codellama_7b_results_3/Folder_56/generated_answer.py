
def all_neg_ints_inclusive(my_list):
    negative_ints = []
    for i in range(len(my_list)):
        if my_list[i] < 0:
            negative_ints.append(my_list[i])
    return negative_ints
