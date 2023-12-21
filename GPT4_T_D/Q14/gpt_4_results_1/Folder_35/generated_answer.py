
def find_second_smallest_num(num_list):
    if len(num_list) >= 40:
        sliced_list = num_list[15:40]
        sliced_list.sort()
        if len(sliced_list) >= 2:
            return sliced_list[1]
    return None
