
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of the element that comes after index 76 in my_list
    next_index = my_list.index(10.01, 76) + 1
    # Insert 10.01 at the index found above
    new_list.insert(next_index, 10.01)
    return new_list
