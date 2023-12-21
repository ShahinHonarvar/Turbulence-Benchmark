
def insert_after_index(test_list):
    result_list = list(test_list)
    result_list.insert(result_list.index(87) + 1, [78, 16])
    return result_list
