
def find_second_smallest_num(num_list):
    try:
        slice_list = num_list[20:31]
        slice_list.sort()
        return slice_list[1]
    except IndexError:
        return None
