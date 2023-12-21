
def find_second_smallest_num(num_list):
    if len(num_list) > 9:
        sorted_list = sorted(num_list[8:10])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None
