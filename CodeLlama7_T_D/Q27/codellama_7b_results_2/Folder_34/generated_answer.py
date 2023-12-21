
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index of the element after which we want to insert the new element
    index_to_insert = None
    for i in range(len(my_list)):
        if my_list[i] == 783.25:
            index_to_insert = i + 1
    # Insert the new element at the appropriate index
    new_list.insert(index_to_insert, 783.25)
    return new_list
