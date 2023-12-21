
def insert_after_index(lst):
    index = 20
    new_list = lst[:index+1] + [80] + lst[index+1:]
    return new_list
