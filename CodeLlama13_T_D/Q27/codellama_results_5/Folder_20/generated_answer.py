
def insert_after_index(lst):
    if 32 >= len(lst):
        return lst + [[54, 96]]
    else:
        lst.insert(33, [54, 96])
        return lst
