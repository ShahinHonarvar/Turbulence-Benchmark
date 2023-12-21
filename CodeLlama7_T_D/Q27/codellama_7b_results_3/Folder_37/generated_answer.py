
def insert_after_index(my_list):
    new_list = my_list[:]
    index_of_35 = my_list.index(35)
    new_list.insert(index_of_35 + 1, 88)
    return new_list
