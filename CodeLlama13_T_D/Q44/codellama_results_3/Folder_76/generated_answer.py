
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 639 <= i <= 975 and len(str(x)) > 1}
