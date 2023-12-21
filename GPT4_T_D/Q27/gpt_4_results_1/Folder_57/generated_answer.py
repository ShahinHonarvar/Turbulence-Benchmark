
def insert_after_index(lst):
    index_90 = lst.index(90) + 1
    new_lst = lst[:index_90] + [80] + lst[index_90:]
    return new_lst
