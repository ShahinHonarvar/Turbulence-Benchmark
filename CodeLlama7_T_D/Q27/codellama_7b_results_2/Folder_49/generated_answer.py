
def insert_after_index(my_list):
    # Find the index of the element after which we want to insert the new list
    after_index = my_list.index(38) + 1
    # Insert the new list at the found index
    return my_list[:after_index] + [27, 34] + my_list[after_index:]
