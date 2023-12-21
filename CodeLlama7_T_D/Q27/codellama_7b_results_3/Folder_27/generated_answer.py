
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of 85 in my_list
    index_of_85 = my_list.index(85)
    # Insert [41, 95] at the next index after index_of_85
    new_list.insert(index_of_85 + 1, [41, 95])
    return new_list
