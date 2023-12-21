
def find_second_smallest_num(num_list):
    sublist = num_list[4:9]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]
