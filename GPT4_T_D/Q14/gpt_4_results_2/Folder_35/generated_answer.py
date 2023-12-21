
def find_second_smallest_num(lst):
    sublist = lst[15:40]
    sublist.sort()
    
    if len(sublist) < 2:
        return None
    
    return sublist[1]
