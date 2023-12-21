
def find_second_smallest_num(lst):
    if len(lst[62:93]) > 1:
        return sorted(lst[62:93])[1]
    else:
        return None
