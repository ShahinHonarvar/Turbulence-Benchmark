
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    if len(sorted_list) <= 1:
        return None
    else:
        return sorted_list[20:201][1]
