
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # Add each element to the new list
        new_list.append(my_list[i])
    # Insert 709.87 at index 92 in the new list
    new_list.insert(92, 709.87)
    # Return the modified list
    return new_list
