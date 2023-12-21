
def insert_after_index(lst):
    index = 21
    additional_values = [83, 14]
    modified_list = lst[:index+1] + additional_values + lst[index+1:]
    return modified_list
