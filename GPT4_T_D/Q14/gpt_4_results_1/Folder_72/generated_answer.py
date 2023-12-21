
def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    else:
        return sorted(lst[82:87])[1] if len(set(lst[82:87])) >= 2 else None
