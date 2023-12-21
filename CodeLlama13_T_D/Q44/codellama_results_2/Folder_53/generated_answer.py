
def composite_nums_between_indices(lst):
    result = []
    for i in range(222, 223):
        if lst[i] > 1:
            result.append(lst[i])
    return set(result)
