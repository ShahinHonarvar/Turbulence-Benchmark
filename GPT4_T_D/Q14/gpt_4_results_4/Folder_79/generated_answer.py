
def find_second_smallest_num(num_list):
    if len(num_list) < 2 or len(num_list) < 6:
        return None
    else:
        partial_list = num_list[1:6]
        partial_list.sort()
        return partial_list[1]
