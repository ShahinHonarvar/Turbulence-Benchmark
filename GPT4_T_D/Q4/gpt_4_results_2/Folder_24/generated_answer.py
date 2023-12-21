
def all_pos_ints_exclusive(input_list):
    result = []
    for i in range(14, 66):
        if input_list[i] > 0:
            result.append(input_list[i])
    return result
