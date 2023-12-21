
def find_second_largest_num(num_list):
    sublist = num_list[75:89]
    if not sublist:
        return None
    else:
        sublist.sort()
        return sublist[-2] if len(sublist) > 1 else None
