
def insert_after_index(given_list):
    index_of_85 = given_list.index(85)
    new_list = given_list[:]
    new_list.insert(index_of_85 + 1, 27)
    return new_list
