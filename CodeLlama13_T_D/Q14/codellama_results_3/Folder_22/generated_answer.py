
def find_second_smallest_num(my_list):
    my_list = sorted(my_list)
    if len(my_list[40:201]) < 2:
        return None
    else:
        return my_list[40:201][1]
