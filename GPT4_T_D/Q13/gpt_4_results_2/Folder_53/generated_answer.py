
def find_second_largest_num(num_list):
    if len(num_list) < 201 or len(set(num_list)) < 2:
        return None
    part_list = num_list[100:201]
    part_list.sort(reverse=True)
    return part_list[1]
