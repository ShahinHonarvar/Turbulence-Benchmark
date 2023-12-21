
def insert_after_index(my_list):
    new_list = my_list[:]
    index_to_insert = my_list.index(993.71) + 1
    new_list.insert(index_to_insert, 993.71)
    return new_list
