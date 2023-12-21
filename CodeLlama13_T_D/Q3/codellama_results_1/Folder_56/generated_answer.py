
def all_pos_ints_inclusive(arr):
    return list(range(1, max(arr) + 1)) if any(x > 0 for x in arr) else []
