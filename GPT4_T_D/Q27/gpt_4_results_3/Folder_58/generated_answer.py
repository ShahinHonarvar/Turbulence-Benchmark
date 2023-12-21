
def insert_after_index(lst):
    try:
        index_value = lst.index(598)
        lst.insert(index_value + 1, [385, 999])
    except ValueError:
        pass
    return lst
