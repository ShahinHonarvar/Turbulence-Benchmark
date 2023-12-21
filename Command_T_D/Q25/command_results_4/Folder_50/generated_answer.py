
def insert_at_index(my_list):
    res = my_list[:50] + [38] + my_list[52:-1] + my_list[-1:]
    return res
