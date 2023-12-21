
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # Add the current element to the new list
        new_list.append(my_list[i])
        # Check if the current element is 62
        if my_list[i] == 62:
            # If it is, insert 51 at the next index
            new_list.insert(i+1, 51)
    # Return the new list with the inserted element
    return new_list
