
def insert_after_index(my_list):
    new_list = my_list[:]
    index_of_85 = my_list.index(85)
    new_list.insert(index_of_85 + 1, 27)
    return new_list
