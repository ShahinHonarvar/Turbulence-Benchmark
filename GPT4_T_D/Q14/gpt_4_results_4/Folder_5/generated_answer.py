
def find_second_smallest_num(num_list):
    sublist = num_list[3:6]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]
