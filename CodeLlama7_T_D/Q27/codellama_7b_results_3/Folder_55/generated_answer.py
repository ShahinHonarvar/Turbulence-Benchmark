
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    try:
        index = my_list.index(141.02) # find the index of the element to be inserted
        new_list.insert(index+1, 141.02) # insert the element at the next index
    except ValueError:
#        print("Element not found in list.")

    return new_list
