
def insert_after_index(lst):
    index = 32
    new_lst = lst[:index + 1] + [54, 96] + lst[index + 1:]
    return new_lst
