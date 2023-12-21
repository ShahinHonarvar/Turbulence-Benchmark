
def find_second_smallest_num(num_list):
    sublist = num_list[246:751]
    if len(sublist)>=2:
        sublist.sort()
        return sublist[1]
    else:
        return None
