
def insert_after_index(input_list):
    new_list = input_list[:]
    if 28 in new_list:
        new_list.insert(new_list.index(28) + 1, 20)
    return new_list
