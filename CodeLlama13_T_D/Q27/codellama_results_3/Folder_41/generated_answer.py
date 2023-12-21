
def insert_after_index(my_list):
    new_list = []
    for i, item in enumerate(my_list):
        if i == 87:
            new_list.extend([item, [78, 16]])
        else:
            new_list.append(item)
    return new_list
