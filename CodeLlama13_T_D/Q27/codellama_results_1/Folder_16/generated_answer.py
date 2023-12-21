
def insert_after_index(mylist):
    index = 983
    value = 369
    new_list = mylist[:index+1] + [value] + mylist[index+1:]
    return new_list
