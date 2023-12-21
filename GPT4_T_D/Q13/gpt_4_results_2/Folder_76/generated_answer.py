
def find_second_largest_num(lst):
    if len(lst[686:988]) < 2:
        return None
    else:
        return sorted(lst[686:988])[-2]
