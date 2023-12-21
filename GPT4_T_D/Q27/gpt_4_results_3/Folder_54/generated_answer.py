
def insert_after_index(list):
    index_43 = list.index(43)
    return list[:index_43+1] + [37] + list[index_43+1:]
