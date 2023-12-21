
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 29 <= i <= 51 and len([y for y in range(1, int(x**0.5)+1) if x % y == 0]) > 1}
