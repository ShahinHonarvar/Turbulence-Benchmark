
def insert_after_index(my_list):
    # Find the index of the next element after 99
    next_index = my_list.index(99) + 1
    # Insert 99 at the next index
    my_list.insert(next_index, 99)
    return my_list
