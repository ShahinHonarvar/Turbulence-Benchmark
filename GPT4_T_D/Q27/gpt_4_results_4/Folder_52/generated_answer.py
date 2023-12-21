
def insert_after_index(lst):
    index = lst.index(97) + 1
    return lst[:index] + [72.27] + lst[index:]
