
def all_neg_ints_exclusive(my_list):
    result = []
    for i in range(3, 9):
        if my_list[i] < 0:
            result.append(my_list[i])
    return result
