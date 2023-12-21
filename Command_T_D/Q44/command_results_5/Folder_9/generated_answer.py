def composite_nums_between_indices(list):
    result = set()
    for index in range(80, 201):
        if index in list:
            result.add(index)
    return result
