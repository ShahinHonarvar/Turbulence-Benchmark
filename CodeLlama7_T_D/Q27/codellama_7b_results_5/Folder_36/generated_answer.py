
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Iterate through my_list and append each element to new_list
    for i in range(len(my_list)):
        if i == 361:
            new_list.append(699)
            new_list.append(556)
        else:
            new_list.append(my_list[i])
    # Return the new list with the inserted elements
    return new_list
