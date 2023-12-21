
def insert_after_index(lst):
    index = 42
    new_list = lst[:index+1] + [53] + lst[index+1:]
    return new_list
