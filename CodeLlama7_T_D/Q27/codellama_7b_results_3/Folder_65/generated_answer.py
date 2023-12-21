
def insert_after_index(my_list):
    # Find the index of the element we want to insert after
    after_index = my_list.index(70) + 1
    # Create a new list with the inserted element
    new_list = my_list[:after_index] + [185.43] + my_list[after_index:]
    return new_list
