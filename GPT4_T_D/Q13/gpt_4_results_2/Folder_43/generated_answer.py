
def find_second_largest_num(num_list):
    if len(num_list) < 87:
        return None
    else:
        partial_list = num_list[68:87]
        partial_list.sort()
        if len(partial_list) < 2:
            return None
        else:
            return partial_list[-2]
