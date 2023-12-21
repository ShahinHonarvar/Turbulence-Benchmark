

def find_second_smallest_num(number_list):
    if len(number_list[90:201]) < 2:
        return None
    else:
        sorted_list = sorted(number_list[90:201])
        return sorted_list[1]
