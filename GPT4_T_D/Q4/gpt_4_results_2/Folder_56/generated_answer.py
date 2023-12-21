
def all_pos_ints_exclusive(integer_list):
    result = []
    for i in range(8, 9):
        if integer_list[i] > 0:
            result.append(integer_list[i])
    return result
