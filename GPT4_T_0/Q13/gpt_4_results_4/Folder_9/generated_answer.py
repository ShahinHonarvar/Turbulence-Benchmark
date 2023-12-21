
def find_second_largest_num(num_list):
    if len(num_list) < 201 or len(num_list[200:201]) < 2:
        return None
    else:
        return sorted(num_list[200:201])[-2]
