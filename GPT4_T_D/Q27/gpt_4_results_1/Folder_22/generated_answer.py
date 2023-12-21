
def insert_after_index(lst):
    index_85 = lst.index(85)
    return lst[:index_85+1] + [27] + lst[index_85+1:]
