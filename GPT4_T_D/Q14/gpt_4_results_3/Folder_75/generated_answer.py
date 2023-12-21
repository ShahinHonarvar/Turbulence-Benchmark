
def find_second_smallest_num(num_list):
    num_range = num_list[12:93]
    
    if len(num_range) < 2:
        return None

    num_range.sort()
    return num_range[1]
