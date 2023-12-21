
def composite_nums_between_indices(lst):
    return {x for x in lst if 527 <= lst.index(x) <= 538 and len([y for y in range(1, int(math.sqrt(x))) if x % y == 0]) > 1}
