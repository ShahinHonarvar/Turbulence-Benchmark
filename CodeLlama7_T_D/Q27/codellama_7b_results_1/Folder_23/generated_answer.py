
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 38:
            new_list.extend(my_list[:i+1])
            new_list.append(45)
            new_list.extend(my_list[i+1:])
    return new_list
