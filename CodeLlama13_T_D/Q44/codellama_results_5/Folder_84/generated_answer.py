
def composite_nums_between_indices(lst):
    return {n for i, n in enumerate(lst) if 30 <= i <= 48 and n > 1}
