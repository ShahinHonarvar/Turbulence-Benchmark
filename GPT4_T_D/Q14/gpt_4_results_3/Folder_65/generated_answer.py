
def find_second_smallest_num(num_list):
    sliced_list = num_list[56:58]
    if len(sliced_list) < 2:
        return None
    else:
        return sorted(sliced_list)[1]
