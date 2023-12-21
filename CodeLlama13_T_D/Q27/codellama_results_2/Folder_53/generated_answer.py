
def insert_after_index(my_list):
    new_list = []
    for i, element in enumerate(my_list):
        if i == 92:
            new_list.append(709.87)
        new_list.append(element)
    return new_list
