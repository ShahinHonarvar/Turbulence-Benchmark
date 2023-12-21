
def find_second_smallest_num(lst):
    sublist = lst[56:58]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[1]
