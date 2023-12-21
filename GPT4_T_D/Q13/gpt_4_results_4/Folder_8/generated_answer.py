
def find_second_largest_num(num_list):
    if len(num_list) < 24:
        return None
    else:
        slice_list = num_list[23:24]
        if len(slice_list) < 2:
            return None
        else:
            slice_list.sort()
            return slice_list[-2]
