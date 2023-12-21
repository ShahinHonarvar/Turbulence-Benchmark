
def insert_at_index(my_list, index, value):
    # Create a new list with the same elements as my_list
    new_list = []
    # Iterate through each element of my_list
    for i in range(len(my_list)):
        # If the current index is equal to the specified index, insert the value at that position
        if i == index:
            new_list.insert(i, value)
        # Otherwise, add the element from my_list to the new list
        else:
            new_list.append(my_list[i])
    # Return the new list with the inserted value
    return new_list
