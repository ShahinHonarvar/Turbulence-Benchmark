
def find_second_largest_num(num_list):
    if len(num_list) < 60:
        return None
    else:
        slice_list = num_list[25:60]
        slice_list.sort(reverse=True)
        return slice_list[1] if len(slice_list) > 1 else None
