
def insert_after_index(my_list):
    # Find the index of the element that we want to insert after
    insertion_index = my_list.index(564) + 1
    # Insert the new element at the found index
    my_list.insert(insertion_index, 149)
    return my_list
