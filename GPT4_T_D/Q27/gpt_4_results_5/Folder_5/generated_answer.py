
def insert_after_index(input_list):
    index = input_list.index(99) if 99 in input_list else None
    if index is not None:
        input_list.insert(index + 1, 15)
    return input_list
