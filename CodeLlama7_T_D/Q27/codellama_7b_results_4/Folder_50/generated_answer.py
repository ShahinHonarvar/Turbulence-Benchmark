
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    try:
        index = my_list.index(38) + 1 # find the index of the element after 38
        new_list.insert(index, 38) # insert 38 at the found index
    except ValueError:
        pass

    return new_list
