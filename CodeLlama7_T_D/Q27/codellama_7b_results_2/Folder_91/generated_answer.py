
def insert_after_index(my_list):
    new_list = my_list[:]
    index_of_2 = my_list.index(2)
    new_list.insert(index_of_2 + 1, 8)
    return new_list
