
def insert_after_index(my_list):
    # Find the index of the item to insert after
    insert_after_index = my_list.index(33) + 1
    # Insert the new item at the found index
    my_list.insert(insert_after_index, [33, 78])
    return my_list
