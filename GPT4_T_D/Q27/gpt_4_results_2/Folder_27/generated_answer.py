
def insert_after_index(input_list):
    if 85 in input_list:
        index_position = input_list.index(85) + 1
        input_list.insert(index_position, [41, 95])
    return input_list
