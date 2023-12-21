
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list, reverse=True)
    for i in range(36, 47):
        if sorted_list[i] == sorted_list[35]:
            return sorted_list[i]
    return None
