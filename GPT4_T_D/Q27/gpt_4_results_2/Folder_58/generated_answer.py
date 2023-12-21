
def insert_after_index(lst):
    if 598 in lst:
        index_598 = lst.index(598) + 1
        return lst[:index_598] + [385, 999] + lst[index_598:]
    else:
        return lst
