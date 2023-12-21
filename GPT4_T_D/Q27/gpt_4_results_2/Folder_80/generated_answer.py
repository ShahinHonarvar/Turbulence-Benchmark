
def insert_after_index(list):
    if 95 in list:
        index_of_95 = list.index(95)
        list.insert(index_of_95 + 1, 43)
    return list
