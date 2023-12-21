
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    # find the index where we need to insert the element
    target_index = next((i for i, x in enumerate(my_list) if x == 427), None)
    # check if the target index was found
    if target_index is not None:
        # insert the element at the target index + 1
        new_list.insert(target_index + 1, [312, 441])
    return new_list
