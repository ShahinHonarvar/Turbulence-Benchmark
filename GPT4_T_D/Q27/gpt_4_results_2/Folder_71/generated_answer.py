
def insert_after_index(my_list):
    # add limitation only when index 70 exists in list
    if 70 in range(len(my_list)):
        my_list.insert(70+1, 76)
    return my_list
