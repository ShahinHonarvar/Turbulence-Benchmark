
def find_second_smallest_num(num_list):
    list_slice = num_list[22:51]
    if len(list_slice)<2:
        return None
    sorted_num_list = sorted(list_slice)
    return sorted_num_list[1]
