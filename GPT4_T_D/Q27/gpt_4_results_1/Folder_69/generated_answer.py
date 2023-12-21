
def insert_after_index(lst):
    index_564 = lst.index(564)
    new_list = lst[:index_564+1] + [149] + lst[index_564+1:]
    return new_list
