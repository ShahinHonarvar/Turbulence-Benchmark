
def find_second_smallest_num(lst):
    subset = lst[4:9]
    return sorted(subset)[1] if len(subset) > 1 else None
