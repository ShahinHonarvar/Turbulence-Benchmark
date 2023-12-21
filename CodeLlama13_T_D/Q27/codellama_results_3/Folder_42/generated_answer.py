
def insert_after_index(lst):
    if 44 in lst:
        index = lst.index(44) + 1
        new_list = lst[:index] + [40, 27] + lst[index:]
        return new_list
    else:
        return lst
