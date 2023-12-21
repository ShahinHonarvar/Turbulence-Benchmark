
def find_second_largest_num(num_list):
    if len(num_list) < 73:
        return None
    else:
        slice_list = num_list[31:73]
        slice_list.sort()
        return slice_list[-2] if len(slice_list) > 1 else None
