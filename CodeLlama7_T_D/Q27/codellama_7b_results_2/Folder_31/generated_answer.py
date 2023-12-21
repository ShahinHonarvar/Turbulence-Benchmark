
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    # find the index where we want to insert the element
    idx = next((i for i, x in enumerate(my_list) if x == 21), None)
    if idx is not None:
        # insert the element at the next index
        new_list.insert(idx + 1, [83, 14])
    return new_list
