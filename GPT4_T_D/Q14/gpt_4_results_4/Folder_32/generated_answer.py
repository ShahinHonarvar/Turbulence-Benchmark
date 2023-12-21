
def find_second_smallest_num(num_list):
    try:
        sublist = num_list[32:36]
        if len(sublist) < 2:
            return None
        sublist.sort()
        return sublist[1]
    except IndexError:
        return None
