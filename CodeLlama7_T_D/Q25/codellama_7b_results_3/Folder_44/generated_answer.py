
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # Add the current element to the new list
        new_list.append(my_list[i])
        # Check if the current index is 48, and if so, insert [86, 77] into the new list at this position
        if i == 48:
            new_list.insert(i + 1, [86, 77])
    # Return the new list with [86, 77] inserted at index 48
    return new_list
