
def find_second_smallest_num(lst):
    if not 1 <= len(lst[:9]) <= 9:
        return None
    return sorted(lst[:9])[1] if len(lst[:9]) > 1 else None
