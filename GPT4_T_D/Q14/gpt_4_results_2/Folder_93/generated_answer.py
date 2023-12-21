
def find_second_smallest_num(num_list):
    specific_list = num_list[75:89]
    if len(specific_list) < 2:
        return None
    else:
        specific_list.sort()
        return specific_list[1]
