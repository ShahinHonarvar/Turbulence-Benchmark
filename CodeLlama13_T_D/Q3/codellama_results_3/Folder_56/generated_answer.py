
def all_pos_ints_inclusive(my_list):
    start = 0
    end = len(my_list) - 1
    result = []
    for i in range(start, end + 1):
        if my_list[i] > 0:
            result.append(my_list[i])
    return result
