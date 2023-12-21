
def find_second_smallest_num(num_list):
    if len(num_list)<94:
        return None
    else:
        sublist = num_list[66:94]
        sublist.sort()
        if len(sublist)>1:
            return sublist[1]
        else:
            return None
