
def insert_after_index(list_given):
    if 62 in list_given:
        index = list_given.index(62)
        list_given.insert(index + 1, 51)
    return list_given
