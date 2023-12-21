
def find_second_smallest_num(my_list):
    if len(my_list) <= 94:
        return None
    sorted_list = sorted(my_list[75:95])
    return sorted_list[1]
