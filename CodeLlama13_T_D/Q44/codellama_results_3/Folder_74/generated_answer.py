
def composite_nums_between_indices(lst):
    result = set()
    for i in range(42, 68+1):
        if len(set(str(lst[i])).intersection('123456789')) > 0:
            result.add(lst[i])
    return result
