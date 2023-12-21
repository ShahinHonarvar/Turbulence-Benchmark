
def find_second_smallest_num(my_list):
    if len(my_list) <= 2 or len(my_list) < 100:
        return None
    else:
        sliced_list = my_list[1:101]
        sliced_list.sort()
        return sliced_list[1]
