
def all_pos_ints_exclusive(my_list):
    result = []
    for i in range(111, 473):
        if my_list[i] > 0:
            result.append(my_list[i])
    return result
