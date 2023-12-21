
def insert_at_index(input_list):
    new_list = input_list[:] # clone the list to prevent modification to original
    new_list.insert(13, [56, 54]) # insert required list at index 13
    return new_list
