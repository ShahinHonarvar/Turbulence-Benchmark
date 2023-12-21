
def find_second_smallest_num(num_list):
    if len(num_list) >= 79:
        sublist = sorted(num_list[17:79])
        if len(sublist) >= 2:
            return sublist[1]
    return None
