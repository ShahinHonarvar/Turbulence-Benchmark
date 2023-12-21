
def insert_after_index(lst):
    try: 
        index_val = lst.index(761)
        lst.insert(index_val + 1, 925)
    except ValueError:
        pass
    return lst
