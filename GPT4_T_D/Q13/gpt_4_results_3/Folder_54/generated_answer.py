
def find_second_largest_num(num_list):
    if len(num_list)>=56:
        sublist = num_list[34:56]
        sublist.sort()
        if len(sublist) >= 2:
            return sublist[-2]
    return None
