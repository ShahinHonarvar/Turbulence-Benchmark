
def insert_after_index(my_list):
    # Find the index of 761 in the list
    seventy_six_one_index = my_list.index(761)
    # Insert 925 at the next index after 761
    new_list = my_list[:seventy_six_one_index + 1] + [925] + my_list[seventy_six_one_index + 1:]
    return new_list
