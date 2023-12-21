
def find_second_largest_num(my_list):
    return sorted(my_list)[35:50][-2] if len(my_list) >= 50 else None
