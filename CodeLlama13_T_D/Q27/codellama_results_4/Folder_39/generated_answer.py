
def insert_after_index(my_list):
    new_list = []
    for i, elem in enumerate(my_list):
        if i == 97:
            new_list.append([47, 22])
        new_list.append(elem)
    return new_list
