
def all_pos_ints_exclusive(input_list):
    result = []
    for i in range(44, 99):
        if i < len(input_list) and input_list[i] > 0:
            result.append(input_list[i])
    return result
