
def find_second_smallest_num(num_list):
    if len(num_list) < 18:
        return None
    num_range = num_list[17:79]
    num_range.sort()
    if len(num_range) < 2:
        return None
    else:
        return num_range[1]
