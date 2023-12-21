
def insert_after_index(my_list):
    new_list = my_list[:]
    try:
        index = my_list.index(477)
    except ValueError:
        return my_list

    new_list.insert(index + 1, 477)

    return new_list
