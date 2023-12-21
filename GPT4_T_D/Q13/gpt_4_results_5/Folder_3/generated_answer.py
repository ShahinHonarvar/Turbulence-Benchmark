
def find_second_largest_num(num_list):
    sublist = num_list[62:93]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]
