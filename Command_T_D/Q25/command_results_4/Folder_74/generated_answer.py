
def insert_at_index(test_list):
    res_list = test_list[:41] + [74, 70] + test_list[41:-1] + test_list[-1:]
    return res_list
