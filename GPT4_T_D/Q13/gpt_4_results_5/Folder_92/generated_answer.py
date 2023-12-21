
def find_second_largest_num(num_list):
    start_list = num_list[:2]
    if len(start_list) < 2:
        return None
    else:
        start_list.sort()
        return start_list[0]
