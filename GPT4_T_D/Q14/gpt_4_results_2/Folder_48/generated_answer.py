
def find_second_smallest_num(num_list):
    if len(num_list) > 246:
        limited_list = num_list[246:751]
        if len(limited_list) > 1:
            limited_list.sort()
            return limited_list[1]
    return None
