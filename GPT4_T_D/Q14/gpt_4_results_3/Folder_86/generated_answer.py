
def find_second_smallest_num(num_list):
    sublist = num_list[33:37]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[1]
