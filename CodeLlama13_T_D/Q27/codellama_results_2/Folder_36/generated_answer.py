
def insert_after_index(my_list):
    if 361 < len(my_list):
        return my_list[:362] + [699, 556] + my_list[362:]
    else:
        return my_list[:362] + [699, 556]
