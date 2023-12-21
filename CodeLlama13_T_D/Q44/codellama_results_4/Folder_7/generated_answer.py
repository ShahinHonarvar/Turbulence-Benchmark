
def composite_nums_between_indices(list):
    result = []
    for i in range(527, 539):
        if list[i] > 1 and not isinstance(list[i], bool) and not isinstance(list[i], str):
            result.append(list[i])
    return set(result)
