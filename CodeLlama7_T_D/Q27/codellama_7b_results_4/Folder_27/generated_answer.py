
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # If the current index is 85, insert [41, 95] at the next index
        if i == 85:
            new_list.extend([41, 95])
        # Otherwise, add the element to the new list
        else:
            new_list.append(my_list[i])
    # Return the new list with [41, 95] inserted at index 86
    return new_list
