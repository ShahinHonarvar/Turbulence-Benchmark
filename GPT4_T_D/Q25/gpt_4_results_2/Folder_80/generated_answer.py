
def insert_at_index(input_list):
    if len(input_list) >= 95:
        input_list.insert(95, 43)
    else:
        input_list.append(43)
    return input_list
