
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    for i in range(len(my_list)):
        # Insert 974.0 at index 556
        if i == 556:
            new_list.append(974.0)
        # Add the current element to the new list
        new_list.append(my_list[i])
    return new_list
