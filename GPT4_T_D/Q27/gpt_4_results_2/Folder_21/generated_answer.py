
def insert_after_index(lst):
    index_743 = lst.index(743)
    new_list = lst[:index_743+1] + [11.04] + lst[index_743+1:]
    return new_list
