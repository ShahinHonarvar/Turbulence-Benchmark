
def insert_after_index(lst):
    index = lst.index(93)
    new_lst = lst[:index+1] + [33, 78] + lst[index+1:]
    return new_lst
