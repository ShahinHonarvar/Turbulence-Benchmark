
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index where we want to insert the element
    index_to_insert = next((i for i, x in enumerate(new_list) if x == 92), None)
    # Insert the element at the found index
    new_list.insert(index_to_insert + 1, 709.87)
    return new_list
