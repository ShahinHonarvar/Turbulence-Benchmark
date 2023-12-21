
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Loop through each element in my_list
    for i in range(len(my_list)):
        # If the current index is 38, insert [27, 34] at the next index
        if i == 38:
            new_list.extend(my_list[i:])
            new_list.insert(i + 1, [27, 34])
            break

    # If the current index is not 38, append the element to the new list
    else:
        for elem in my_list:
            new_list.append(elem)

    return new_list
