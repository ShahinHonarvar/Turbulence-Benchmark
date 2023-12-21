
def find_second_largest_num(num_list):
    if len(num_list)<606:
        return None
    else:
        sublist = num_list[533:606]
        sublist.sort()
        return sublist[-2]
