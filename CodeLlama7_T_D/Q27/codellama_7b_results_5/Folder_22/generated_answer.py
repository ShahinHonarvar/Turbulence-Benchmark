
def insert_after_index(my_list):
    new_list = my_list[:] # Make a copy of the list
    # Find the index where 27 should be inserted
    index = next((i for i, x in enumerate(my_list) if x == 85), None)
    # Insert 27 at the next index after 85
    new_list.insert(index + 1, 27)
    return new_list
