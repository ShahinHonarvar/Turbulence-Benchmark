
def all_neg_ints_exclusive(my_list):
    for index, value in enumerate(my_list):
        if value < 0:
            return my_list[index+1:]
    return []
