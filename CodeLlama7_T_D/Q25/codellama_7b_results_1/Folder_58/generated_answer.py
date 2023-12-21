
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # Add the current element to the new list
        new_list.append(my_list[i])
        # Check if we are at the index where [385, 999] should be inserted
        if i == 598:
            # Insert [385, 999] into the new list
            new_list.extend([385, 999])
    # Return the modified list with [385, 999] inserted at index 598
    return new_list
