
def find_second_largest_num(num_list):
    sublist = num_list[75:95]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]
