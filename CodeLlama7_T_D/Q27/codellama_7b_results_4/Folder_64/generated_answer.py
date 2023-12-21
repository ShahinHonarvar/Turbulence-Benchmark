
def insert_after_index(my_list):
    # Create a new list that is identical to the input list
    new_list = my_list[:]
    # Find the index of the element after which we want to insert our new elements
    index = my_list.index(8) + 1
    # Insert [3, 8] at the index found above
    new_list.insert(index, [3, 8])
    return new_list
