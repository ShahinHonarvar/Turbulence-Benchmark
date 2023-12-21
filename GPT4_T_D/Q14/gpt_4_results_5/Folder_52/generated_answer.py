
def find_second_smallest_num(num_list):
    try:
        sublist = sorted(num_list[64:67])
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]
    except IndexError:
        return None
