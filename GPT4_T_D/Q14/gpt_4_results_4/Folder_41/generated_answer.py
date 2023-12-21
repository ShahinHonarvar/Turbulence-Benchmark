
def find_second_smallest_num(lst):
    if len(lst[4:5]) < 2:
        return None
    else:
        return sorted(lst[4:5])[1]
