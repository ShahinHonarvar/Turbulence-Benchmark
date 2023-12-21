
def insert_after_index(my_list):
    # Create a new list with an extra element
    new_list = my_list[:]
    # Find the index of 66 in the original list
    six_six_index = my_list.index(66)
    # Insert 45 at the next index
    new_list.insert(six_six_index + 1, 45)
    return new_list
