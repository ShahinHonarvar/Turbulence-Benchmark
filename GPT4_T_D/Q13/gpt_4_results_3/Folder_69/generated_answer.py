
def find_second_largest_num(num_list):
    slice_list = num_list[32:36]
    if len(slice_list) == 0:
        return None
    else:
        slice_list.sort()
        return slice_list[-2]
