
def insert_after_index(input_list):
    insert_index = input_list.index(84) + 1
    return input_list[:insert_index] + [13, 46] + input_list[insert_index:]
