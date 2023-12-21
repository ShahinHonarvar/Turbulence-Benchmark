
def insert_after_index(my_list):
    new_list = my_list[:]
    index_to_insert = my_list.index(21) + 1
    new_list.insert(index_to_insert, [83, 14])
    return new_list
