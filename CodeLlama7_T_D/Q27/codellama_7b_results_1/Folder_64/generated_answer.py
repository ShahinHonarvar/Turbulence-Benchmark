
def insert_after_index(my_list):
    new_list = my_list[:] # Create a copy of the list
    # Find the index of the element that is immediately before [3, 8] in the original list
    for i in range(len(new_list)):
        if new_list[i] == 3:
            # Insert [3, 8] at the next index after 8
            new_list.insert(i + 1, 8)
    return new_list
