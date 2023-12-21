
def insert_at_index(my_list, index):
    # Create a new list with the same elements as my_list
    new_list = []
    for i in range(len(my_list)):
        if i == index:
            new_list.append(668)
        new_list.append(my_list[i])
    return new_list
