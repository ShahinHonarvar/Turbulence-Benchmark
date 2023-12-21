
def find_second_smallest_num(lst):
    if len(lst[26:53]) < 2:
        return None
    else:
        return sorted(lst[26:53])[1]
