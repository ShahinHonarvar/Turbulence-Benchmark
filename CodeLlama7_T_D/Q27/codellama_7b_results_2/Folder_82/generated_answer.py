
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Iterate over the elements of my_list
    for i in range(len(my_list)):
        # If the current element is 84, insert 771.92 after it
        if my_list[i] == 84:
            new_list.append(771.92)
        # Otherwise, append the current element to the new list
        else:
            new_list.append(my_list[i])
    # Return the new list with the inserted element
    return new_list
