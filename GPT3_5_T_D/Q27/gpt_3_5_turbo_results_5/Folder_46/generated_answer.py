
def insert_after_index(lst):
    index = 28 # index to insert the value after
    value = 717.02 # value to be inserted
    return lst[:index+1] + [value] + lst[index+1:]
