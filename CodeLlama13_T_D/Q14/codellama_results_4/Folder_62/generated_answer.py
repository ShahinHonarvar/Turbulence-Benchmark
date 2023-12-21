
def find_second_smallest_num(my_list):
    if len(my_list) < 10:
        return None
    sorted_list = sorted(my_list[10:67])
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
