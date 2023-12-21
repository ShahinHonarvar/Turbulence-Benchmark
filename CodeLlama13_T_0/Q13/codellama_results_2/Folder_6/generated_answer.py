
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list, reverse=True)
    for i in range(10, 67):
        if sorted_list[i] == sorted_list[9]:
            continue
        else:
            return sorted_list[i]
    return None
