def all_pos_ints_exclusive(integers):
    result = []
    for index in range(81, 86):
        if index in integers and integers[index] > 0:
            result.append(integers[index])
    return result
