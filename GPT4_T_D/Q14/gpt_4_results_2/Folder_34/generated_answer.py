
def find_second_smallest_num(lst):
    if len(lst) > 60 and len(lst) <= 200:
        return sorted(lst[60:201])[1]
    else:
        return None
