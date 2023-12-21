
def insert_after_index(lst):
    index_55 = lst.index(55)
    return lst[:index_55+1] + [26, 10] + lst[index_55+1:]
