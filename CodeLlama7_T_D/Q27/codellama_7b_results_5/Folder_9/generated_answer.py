
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if i == 66:
            new_list.insert(i+1, 45)
    return new_list
