
def insert_after_index(lst):
    index_74 = lst.index(74)
    return lst[:index_74+1] + [51, 29] + lst[index_74+1:]
