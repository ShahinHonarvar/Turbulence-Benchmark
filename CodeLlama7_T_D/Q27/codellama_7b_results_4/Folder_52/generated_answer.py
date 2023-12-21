
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of the element that is immediately before 97
    before_index = my_list.index(97) - 1
    # Insert 72.27 at the index found above
    new_list.insert(before_index + 1, 72.27)
    return new_list
