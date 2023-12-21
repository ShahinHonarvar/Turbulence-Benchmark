
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 73:
            new_list.extend([418.88, my_list[i + 1]])
        else:
            new_list.append(my_list[i])
    return new_list
