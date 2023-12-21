
def find_second_smallest_num(lst):
    if len(lst) < 40:
        return 'None'
    
    sublist = sorted(lst[15:40])
    if len(sublist) < 2:
        return 'None'
    
    return sublist[1]
