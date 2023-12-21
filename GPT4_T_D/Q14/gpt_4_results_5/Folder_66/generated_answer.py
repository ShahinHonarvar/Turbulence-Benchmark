
def find_second_smallest_num(num_list):
    if len(num_list) < 63:
        return None
    else:
        sublist = num_list[62:100]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
