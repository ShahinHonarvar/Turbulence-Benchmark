
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # If the current index is 166, insert 232 at the next index
        if i == 166:
            new_list.insert(i + 1, 232)
        # Otherwise, add the current element to the new list
        else:
            new_list.append(my_list[i])
    # Return the new list with the inserted element
    return new_list
