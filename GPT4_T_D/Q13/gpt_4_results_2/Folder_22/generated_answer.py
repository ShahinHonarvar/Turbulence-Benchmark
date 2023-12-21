
def find_second_largest_num(lst):
    if len(lst[40:201]) < 2:
        return None
    else:
        return sorted(lst[40:201])[-2]
