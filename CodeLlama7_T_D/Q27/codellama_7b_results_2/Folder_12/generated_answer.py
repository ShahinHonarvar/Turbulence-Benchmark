
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # If the current element is equal to 57, insert 96 at the next index
        if my_list[i] == 57:
            new_list.append(my_list[i])
            new_list.append(96)
        else:
            new_list.append(my_list[i])
    return new_list
