
def insert_after_index(my_list):
    # Find the index of 69 in the list
    index_of_69 = my_list.index(69)
    # Insert 92 at the next index after 69
    new_list = my_list[:index_of_69 + 1] + [92] + my_list[index_of_69 + 1:]
    return new_list
