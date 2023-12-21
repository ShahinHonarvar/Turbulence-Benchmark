
def find_second_smallest_num(num_list):
    if len(num_list) < 60:
        return None
    sorted_list = sorted(num_list[25:60])
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
