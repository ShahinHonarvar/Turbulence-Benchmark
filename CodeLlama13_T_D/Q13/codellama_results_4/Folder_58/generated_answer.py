
def find_second_largest_num(my_list):
    my_list = sorted(my_list)[209:556+1]
    if len(my_list) > 1:
        return my_list[1]
    else:
        return None
