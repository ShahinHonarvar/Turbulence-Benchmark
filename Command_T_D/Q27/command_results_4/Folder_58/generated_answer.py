
def insert_after_index(a_list):
    b_list = a_list[:]
    b_list.insert(b_list.index(598) + 1, 385)
    b_list.insert(b_list.index(598) + 1, 999)
    return b_list
