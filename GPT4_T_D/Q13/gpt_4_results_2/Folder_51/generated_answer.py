
def find_second_largest_num(num_list):
    slice_list = num_list[1:9]
    if len(slice_list) > 1:
        slice_list.sort()
        return slice_list[-2]
    return None
