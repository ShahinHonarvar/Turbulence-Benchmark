
def find_second_largest_num(num_list):
    num_range = num_list[1:6]
    if len(num_range) < 2:
        return None
    else:
        num_range.sort()
        return num_range[-2]
