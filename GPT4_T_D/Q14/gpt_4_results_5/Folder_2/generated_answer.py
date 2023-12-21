
def find_second_smallest_num(num_list):
    sublist = num_list[43:87]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[1]
