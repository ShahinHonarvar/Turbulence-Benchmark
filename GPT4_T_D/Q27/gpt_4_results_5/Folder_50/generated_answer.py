
def insert_after_index(lst):
    try:
        index_52 = lst.index(52)
    except ValueError:
        return lst
    return lst[:index_52+1] + [38] + lst[index_52+1:]
