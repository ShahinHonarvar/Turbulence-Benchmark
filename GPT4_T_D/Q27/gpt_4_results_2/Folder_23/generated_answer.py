
def insert_after_index(a_list):
    try:
        index = a_list.index(38)
        a_list.insert(index + 1, 45)
    except ValueError:
        pass
    return a_list
