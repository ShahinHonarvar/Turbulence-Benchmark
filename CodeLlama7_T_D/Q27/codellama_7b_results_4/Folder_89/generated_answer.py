
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 62:
            new_list.extend(my_list[:i+1])
            new_list.insert(i+1, 51)
            new_list.extend(my_list[i+1:])
    return new_list
