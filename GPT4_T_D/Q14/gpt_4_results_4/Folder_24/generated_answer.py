
def find_second_smallest_num(num_list):
    try:
        slice_list = sorted(num_list[23:24])
        if len(slice_list) < 2:
            return None
        else:
            return slice_list[1]
    except IndexError:
        return None
