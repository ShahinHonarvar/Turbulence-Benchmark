
def insert_after_index(my_list):
    # Find the index of the element you want to insert after
    index_to_insert_after = my_list.index(43) + 1
    # Insert the new element at the found index
    my_list.insert(index_to_insert_after, 37)
    return my_list
