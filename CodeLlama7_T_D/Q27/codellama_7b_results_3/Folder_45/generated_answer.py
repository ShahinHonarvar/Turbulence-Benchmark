
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Iterate through the elements of my_list
    for i in range(len(my_list)):
        # If the current index is 84, insert [13, 46] at the next index
        if i == 84:
            new_list.extend([13, 46])
        # Otherwise, add the current element to the new list
        else:
            new_list.append(my_list[i])
    # Return the new list with [13, 46] inserted at index 85
    return new_list
