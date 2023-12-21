
def insert_after_index(my_list):
    new_list = my_list[:]
    index_to_insert = next((i for i, x in enumerate(my_list) if x == 87), None)
    if index_to_insert is not None:
        new_list.insert(index_to_insert + 1, [78, 16])
    return new_list
