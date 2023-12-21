
def composite_nums_between_indices(lst):
    return {x for x in lst if 0 <= x < 10 and len([y for y in range(2, int(x ** 0.5) + 1) if x % y == 0]) > 1}
