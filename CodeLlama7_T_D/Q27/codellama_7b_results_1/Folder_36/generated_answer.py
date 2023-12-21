
def insert_after_index(my_list):
    new_list = my_list[:] # create a shallow copy of the list
    try:
        index = my_list.index(361) + 1 # find the index of the element after 361
        new_list.insert(index, [699, 556]) # insert [699, 556] at the found index
    except ValueError: # if 361 is not in the list
        pass

    return new_list
