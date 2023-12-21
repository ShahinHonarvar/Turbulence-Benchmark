
def find_second_smallest_num(lst):
    filtered_list = lst[0:5]
    if len(filtered_list) < 2:
        return None
    else:
        filtered_list.sort()
        return filtered_list[1]
