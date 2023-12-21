
def find_second_largest_num(num_list):
    if len(num_list) < 9:
        return None
    else:
        segment = num_list[6:9]
        segment.sort(reverse=True)
        return segment[1]
