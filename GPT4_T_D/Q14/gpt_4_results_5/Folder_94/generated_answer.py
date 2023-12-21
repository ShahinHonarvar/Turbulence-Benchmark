
def find_second_smallest_num(num_list):
    if len(num_list) < 72:
        return None
    else:
        sublist = sorted(num_list[52:72])
        if len(sublist) > 1:
            return sublist[1]
        else:
            return None
