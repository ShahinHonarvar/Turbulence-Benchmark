
def find_second_smallest_num(num_list):
    try:
        sliced_list = num_list[37:77]
        sorted_sliced_list = sorted(set(sliced_list))
        if len(sorted_sliced_list) < 2:
            return None
        else:
            return sorted_sliced_list[1]
    except:
        return None
