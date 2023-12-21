
def find_second_smallest_num(num_list):
    try:
        sublist = num_list[23:24]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[1]
        else:
            return None
    except IndexError:
        return None
