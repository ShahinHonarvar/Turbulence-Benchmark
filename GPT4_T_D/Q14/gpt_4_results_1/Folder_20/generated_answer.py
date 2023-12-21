
def find_second_smallest_num(num_list):
    num_sublist = num_list[75:95]
    if len(num_sublist) < 2:
        return None
    else:
        num_sublist.sort()
        return num_sublist[1]
