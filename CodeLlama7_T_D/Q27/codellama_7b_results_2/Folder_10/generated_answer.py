
def insert_after_index(my_list):
    # Find the index of 56 in the list
    index_of_56 = my_list.index(56)
    # Insert 54 at the next index after 56
    new_list = my_list[:index_of_56 + 1] + [54] + my_list[index_of_56 + 1:]
    return new_list
