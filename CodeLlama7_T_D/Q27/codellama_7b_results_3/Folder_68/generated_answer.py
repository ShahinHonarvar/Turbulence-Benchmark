
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of the last element in the list
    last_index = len(new_list) - 1
    # Insert [1, 7] at the next index after the last index
    new_list.insert(last_index + 1, [1, 7])
    return new_list
