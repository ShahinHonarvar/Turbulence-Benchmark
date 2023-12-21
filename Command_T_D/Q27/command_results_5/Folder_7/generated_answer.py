
def insert_after_index(test_list):
    result_list = test_list[:]
    result_list.insert(test_list.index(323) + 1, [389, 303])
    return result_list
