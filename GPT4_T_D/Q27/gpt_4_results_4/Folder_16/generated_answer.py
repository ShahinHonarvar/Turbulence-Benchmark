
def insert_after_index(given_list):
    if 983 in given_list:
        index_value = given_list.index(983) + 1
        given_list.insert(index_value, 369)
    return given_list
