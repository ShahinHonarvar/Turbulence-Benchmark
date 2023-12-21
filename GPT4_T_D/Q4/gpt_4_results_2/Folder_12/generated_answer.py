
def all_pos_ints_exclusive(lst):
    min_index = max(0, 23)
    max_index = min(len(lst), 45)
    return [x for x in lst[min_index:max_index] if x > 0]
