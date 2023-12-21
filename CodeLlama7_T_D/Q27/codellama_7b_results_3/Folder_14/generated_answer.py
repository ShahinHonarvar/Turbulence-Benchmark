
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index of the element after which we want to insert the new element
    idx = my_list.index(550.97) + 1
    # Insert the new element at the found index
    new_list.insert(idx, 550.97)
    return new_list
