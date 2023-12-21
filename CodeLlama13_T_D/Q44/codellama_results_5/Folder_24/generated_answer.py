
def composite_nums_between_indices(lst):
    return {i for i in lst[34:56] if len([d for d in range(2, int(i**0.5) + 1) if i % d == 0]) > 1}
