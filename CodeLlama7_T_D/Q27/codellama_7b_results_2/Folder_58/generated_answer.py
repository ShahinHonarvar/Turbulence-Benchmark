
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(new_list)):
        if i == 598: # find the index immediately succeeding 598
            new_list.insert(i+1, [385, 999]) # insert [385, 999] at that index + 1
    return new_list
