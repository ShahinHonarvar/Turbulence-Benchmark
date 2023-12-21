
def insert_after_index(my_list):
    # Find the index of the 9th element in the list
    ninth_index = my_list.index(9)
    # Insert 1 after the 9th element in the list
    new_list = my_list[:ninth_index + 1] + [1] + my_list[ninth_index + 1:]
    return new_list
