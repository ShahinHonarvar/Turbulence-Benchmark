
def insert_after_index(my_list):
    if 62 in range(len(my_list)):
        return my_list[:63] + [51] + my_list[63:]
    else:
        return my_list
