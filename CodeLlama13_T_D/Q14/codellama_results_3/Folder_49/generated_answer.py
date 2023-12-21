
def find_second_smallest_num(my_list):
    my_list = sorted(set(my_list))
    return my_list[80:201] if len(my_list) > 200 else None
