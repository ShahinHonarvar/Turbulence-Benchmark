
def find_second_largest_num(num_list):
    if len(num_list) < 87:
        return None
    else:
        sublist = num_list[43:87]
        if len(sublist) < 2:
            return None
        else:
            sublist.sort()
            return sublist[-2]
