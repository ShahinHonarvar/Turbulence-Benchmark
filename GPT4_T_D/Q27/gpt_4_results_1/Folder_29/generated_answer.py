
def insert_after_index(input_list):
    if 96 in input_list:
        index = input_list.index(96) + 1
        input_list.insert(index, 36)
    return input_list
