
def find_second_smallest_num(num_list):
    if len(num_list) < 40:
        return None
    else:
        sublist = num_list[28:41]
        sublist.sort()
        if len(sublist) >= 2:
            return sublist[1]
        else:
            return None
