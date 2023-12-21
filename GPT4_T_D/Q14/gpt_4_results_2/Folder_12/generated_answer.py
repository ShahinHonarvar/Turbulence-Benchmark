
def find_second_smallest_num(num_list):
    slice_list = num_list[31:73]
    if len(slice_list) < 2:
        return None
    else:
        slice_list.sort()
        return slice_list[1]
