
def all_pos_ints_inclusive(my_list):
    result = []
    for i in range(1, 6):
        if my_list[i-1] > 0:
            result.append(my_list[i-1])
    return result
