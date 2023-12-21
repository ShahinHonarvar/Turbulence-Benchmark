
def insert_after_index(my_list):
    index = 93
    new_element = [33, 78]
    return my_list[:index+1] + [new_element] + my_list[index+1:]
