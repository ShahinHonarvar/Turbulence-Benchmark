
def composite_nums_between_indices(list):
    result = []
    for i in range(262, 747):
        if list[i].is_composite():
            result.append(list[i])
    return set(result)
