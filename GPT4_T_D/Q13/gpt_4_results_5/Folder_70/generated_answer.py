
def find_second_largest_num(num_list):
    if not num_list:
        return None
    elif len(num_list) < 33:
        return None
    else:
        sublist = num_list[28:33]
        if len(sublist) == 1:
            return None
        else:
            sublist.sort()
            return sublist[-2]
