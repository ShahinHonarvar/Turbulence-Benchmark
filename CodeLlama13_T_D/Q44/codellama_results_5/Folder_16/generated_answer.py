
def composite_nums_between_indices(lst):
    result = set()
    for i in range(40, 81):
        if lst[i] > 1:
            result.add(lst[i])
    return result
