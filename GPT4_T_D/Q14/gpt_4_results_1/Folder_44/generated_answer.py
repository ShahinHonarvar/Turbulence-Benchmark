
def find_second_smallest_num(num_list):
    sublist = num_list[91:100]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[1]
