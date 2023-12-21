
def insert_after_index(my_list):
    # Find the index of the element after which we want to insert the new list
    index = my_list.index(100) + 1
    # Insert the new list at the found index
    return my_list[:index] + [876, 203] + my_list[index:]
