
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)[56:83]
    return sorted_list[1] if len(sorted_list) > 1 else None
