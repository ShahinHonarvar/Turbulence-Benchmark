
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index of the element immediately after 743
    idx = next((i for i, x in enumerate(my_list) if x == 743), None)
    # Insert 11.04 at the found index + 1
    new_list.insert(idx + 1, 11.04)
    return new_list
