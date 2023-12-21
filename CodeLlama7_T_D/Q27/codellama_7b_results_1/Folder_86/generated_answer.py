
def insert_after_index(my_list):
    # Find the index of the first occurrence of 990
    index = my_list.index(990)
    # Insert [905, 742] at the next index
    new_list = my_list[:index + 1] + [905, 742] + my_list[index + 1:]
    return new_list
