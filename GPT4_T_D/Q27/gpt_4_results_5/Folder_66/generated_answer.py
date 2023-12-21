
def insert_after_index(lst):
    # Find index of 62
    index_62 = lst.index(62)+1
    # Insert [19, 13] after index 62
    lst.insert(index_62, [19, 13])
    
    return lst
