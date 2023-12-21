
def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 747:
        return None
    slice_list = num_list[262:747]
    slice_list.sort()
    return slice_list[-2]
