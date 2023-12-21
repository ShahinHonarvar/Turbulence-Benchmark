
def composite_nums_between_indices(lst):
    result = []
    for i in range(10, 101):
        if lst[i] > 1 and lst[i] <= len(lst):
            result.append(lst[i])
    return set(result)
