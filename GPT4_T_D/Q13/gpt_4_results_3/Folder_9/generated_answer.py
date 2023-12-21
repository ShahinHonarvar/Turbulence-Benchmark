
def find_second_largest_num(num_list):
    if len(num_list[200:201]) < 2:
        return None
    else:
        return sorted(num_list[200:201])[-2]
