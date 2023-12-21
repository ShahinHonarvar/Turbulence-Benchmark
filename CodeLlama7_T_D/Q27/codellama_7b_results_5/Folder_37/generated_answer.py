
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the original list
    index = my_list.index(35) + 1 # find the index of 35 and add 1 to get the index of the element that should be inserted after it
    new_list.insert(index, 88) # insert 88 at the index found above
    return new_list
