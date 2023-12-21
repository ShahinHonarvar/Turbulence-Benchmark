
def find_second_smallest_num(num_list):
    try:
        selected_list = num_list[68:87]
        selected_list.sort()
        return selected_list[1]
    except IndexError:
        return None
