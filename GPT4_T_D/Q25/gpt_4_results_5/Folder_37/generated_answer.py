
def insert_at_index(input_list):
    if len(input_list) >= 35:
      input_list.insert(35, 88)
    else:
      input_list.append(88)
    return input_list
