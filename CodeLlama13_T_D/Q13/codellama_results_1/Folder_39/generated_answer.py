
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list, reverse=True)
    second_largest_index = 1
    for i in range(20, 31):
        if sorted_list[i] == sorted_list[second_largest_index]:
            return sorted_list[i]
    return None
