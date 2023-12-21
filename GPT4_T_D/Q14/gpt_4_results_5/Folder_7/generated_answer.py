
def find_second_smallest_num(lst):
    if len(lst) < 988:
        return None
    items = sorted(lst[686:988])
    if len(items) > 1:
        return items[1]
    else:
        return None
