
def find_second_smallest_num(num_list):
    if len(num_list) < 9:
        return None
    else:
        sliced_list = num_list[4:9]
        sliced_list.sort()
        return sliced_list[1] if len(sliced_list) > 1 else None
