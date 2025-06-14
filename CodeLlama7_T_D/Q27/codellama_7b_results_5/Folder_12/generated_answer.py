
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through my_list and append each element to new_list
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    # Insert 96 at the index immediately succeeding index 57
    new_list.insert(new_list.index(57) + 1, 96)
    # Return the new list with 96 inserted at the correct index
    return new_list
