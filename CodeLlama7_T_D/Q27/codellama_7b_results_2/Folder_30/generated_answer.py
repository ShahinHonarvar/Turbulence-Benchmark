
def insert_after_index(my_list):
    new_list = my_list[:]
    # Get the index of the element immediately succeeding index 18
    index = next((i for i, x in enumerate(my_list) if x == 18), None)
    # Insert 742.2 at that index
    new_list.insert(index + 1, 742.2)
    return new_list
