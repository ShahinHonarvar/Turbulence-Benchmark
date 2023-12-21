
def find_second_smallest_num(my_list):
    return sorted(set(my_list[42:69]))[1] if len(sorted(set(my_list[42:69]))) > 1 else None
