
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 62 <= i <= 92 and len([d for d in range(2, int(x**0.5)) if x % d == 0]) > 1}
