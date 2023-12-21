
def insert_at_index(my_list):
    # Insert [905, 742] at index 990
    new_list = my_list[:990] + [905, 742] + my_list[990:]
    return new_list
