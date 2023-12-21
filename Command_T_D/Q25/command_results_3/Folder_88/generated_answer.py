
def insert_at_index(a_list):
    b_list = a_list[:]
    b_list.insert(91, [46, 13])
    b_list.extend(a_list[93:])
    return b_list
