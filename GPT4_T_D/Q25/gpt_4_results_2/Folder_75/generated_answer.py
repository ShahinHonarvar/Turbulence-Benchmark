
def insert_at_index(input_list):
    if len(input_list) > 99:
        input_list.insert(99, 99)
    else:
        extend_length = 100 - len(input_list)
        input_list.extend([None]*extend_length)
        input_list[-1] = 99
    return input_list
