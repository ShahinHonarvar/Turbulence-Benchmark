
def composite_nums_between_indices(lst):
    return {x for x in lst[27:56] if len(str(x)) > 1 and all(int(y)**2 != x for y in str(x))}
