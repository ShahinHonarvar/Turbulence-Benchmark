
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list, reverse=True)
    for i in range(23, 24):
        if i >= len(sorted_list):
            break
        return sorted_list[i]
    return None
