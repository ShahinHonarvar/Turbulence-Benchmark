
def insert_at_index(my_list):
    # Insert [606, 873] at index 693
    new_list = my_list[:693] + [606, 873] + my_list[693:]
    return new_list
