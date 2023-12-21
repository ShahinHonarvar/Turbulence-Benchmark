
def composite_nums_between_indices(lst):
    return {n for i, n in enumerate(lst) if 50 <= i <= 54 and len(str(n)) > 1}
