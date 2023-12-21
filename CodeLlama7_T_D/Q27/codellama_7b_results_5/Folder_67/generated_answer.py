
def insert_after_index(my_list):
    # Find the index of the element we want to insert after
    after_index = my_list.index(44) + 1
    # Insert the new element at the found index
    my_list.insert(after_index, 76)
    return my_list
