
def composite_nums_between_indices(my_list):
    result = set()
    for i in range(12, 93):
        if my_list[i] > 1 and my_list[i] not in result:
            result.add(my_list[i])
    return result
