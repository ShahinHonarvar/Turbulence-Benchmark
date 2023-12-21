
def find_second_largest_num(lst):
    if len(lst)<96:
        return None
    else:
        sublist = lst[74:96]
        sublist.sort()
        return sublist[-2]
