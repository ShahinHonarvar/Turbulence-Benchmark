
def find_second_smallest_num(num_list):
    if len(num_list[75:89]) < 2:
        return None
    sorted_list = sorted(num_list[75:89])
    return sorted_list[1]
