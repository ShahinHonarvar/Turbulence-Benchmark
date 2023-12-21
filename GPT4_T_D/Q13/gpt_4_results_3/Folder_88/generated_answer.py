
def find_second_largest_num(num_list):
    if len(num_list) < 9:
        return None
    else:
        slice_list = num_list[4:9]
        slice_list.sort()
        return slice_list[-2]
