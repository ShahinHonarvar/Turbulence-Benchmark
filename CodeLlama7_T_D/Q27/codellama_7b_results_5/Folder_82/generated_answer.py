
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # If the current index is 84, insert 771.92 at the next index
        if i == 84:
            new_list.append(my_list[i])
            new_list.append(771.92)
        else:
            # Otherwise, add the current element to the new list
            new_list.append(my_list[i])
    # Return the new list with 771.92 inserted at index 85
    return new_list
