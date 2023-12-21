
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index of the element after which we want to insert
    for i in range(len(my_list)):
        if my_list[i] == 13:
            new_list.insert(i + 1, [56, 54])
    return new_list
