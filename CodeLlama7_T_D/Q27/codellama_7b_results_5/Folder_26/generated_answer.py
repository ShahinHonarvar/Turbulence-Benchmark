
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index_to_insert_after = 55
    if index_to_insert_after < len(my_list) - 1:
        new_list.insert(index_to_insert_after + 1, [26, 10])
    return new_list
