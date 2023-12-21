
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index where we want to insert the element
    target_index = 183 + 1
    # Insert the element at the target index
    new_list.insert(target_index, [148, 145])
    return new_list
