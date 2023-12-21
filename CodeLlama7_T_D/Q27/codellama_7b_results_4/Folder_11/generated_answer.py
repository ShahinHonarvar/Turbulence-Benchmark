
def insert_after_index(my_list):
    new_list = my_list[:]
    try:
        index = my_list.index(169.26)
        if index == len(my_list) - 1:
            raise ValueError("Index of 169.26 is at the end of the list")
        new_list.insert(index + 1, 169.26)
    except ValueError as e:
#        print(e)

    return new_list
