
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 53:
            new_list.extend([783.25, my_list[i]])
        else:
            new_list.append(my_list[i])
    return new_list
