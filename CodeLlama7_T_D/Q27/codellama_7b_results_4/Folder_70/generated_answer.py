
def insert_after_index(my_list):
    new_list = my_list[:]
    index_412 = my_list.index(412)
    new_list.insert(index_412 + 1, 668)
    return new_list
