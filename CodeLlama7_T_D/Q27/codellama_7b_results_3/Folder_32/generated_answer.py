
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # Append the current element to the new list
        new_list.append(my_list[i])
        # Check if the current index is 76, indicating that we want to insert the new element after this index
        if i == 76:
            # Insert the new element at the next index in the loop
            new_list.insert(i + 1, 10.01)
    # Return the new list with the inserted element
    return new_list
