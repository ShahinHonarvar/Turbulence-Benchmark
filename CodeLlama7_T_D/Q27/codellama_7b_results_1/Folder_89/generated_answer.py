
def insert_after_index(my_list):
    # Create a new list that is identical to the original list
    new_list = my_list[:]
    # Find the index of the element after which we want to insert 51
    insertion_index = next((i for i, x in enumerate(my_list) if x == 62), None)
    # Insert 51 at the found index
    new_list.insert(insertion_index + 1, 51)
    return new_list
