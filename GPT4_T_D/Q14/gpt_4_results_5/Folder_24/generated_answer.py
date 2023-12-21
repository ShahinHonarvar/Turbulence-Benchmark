
def find_second_smallest_num(numbers_list):
    if len(numbers_list[23:24]) < 2:
        return None
    else:
        return sorted(numbers_list[23:24])[1]
