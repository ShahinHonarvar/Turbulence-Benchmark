
def insert_after_index(given_list):
    if 85 in given_list:
        new_index = given_list.index(85) + 1
        given_list.insert(new_index, [41, 95])
    return given_list
