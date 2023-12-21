
def insert_at_index(my_list):
    # Insert [389, 303] at index 323
    new_list = my_list[:323] + [389, 303] + my_list[323:]
    return new_list
