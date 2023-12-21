
def insert_after_index(my_list):
    new_list = my_list[:] # Create a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 42: # Check if the current element is 42
            new_list.insert(i + 1, 53) # Insert 53 at the next index after 42
    return new_list
