
def find_second_largest_num(num_list):
    partial_list = num_list[0:3]
    if len(partial_list) < 2:
        return None
    else:
        partial_list.sort()
        return partial_list[-2]
