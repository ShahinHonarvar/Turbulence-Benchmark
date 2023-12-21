
def find_smallest_num(num_list):
    if len(num_list) - 1 >= 23:
        return min(num_list[23:24])
    else:
        return None
