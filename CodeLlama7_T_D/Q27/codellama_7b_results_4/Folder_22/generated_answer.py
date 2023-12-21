
def insert_after_index(my_list):
    new_list = []
    for i, elem in enumerate(my_list):
        if i == 85:
            new_list.append(elem)
            new_list.append(27)
        else:
            new_list.append(elem)
    return new_list
