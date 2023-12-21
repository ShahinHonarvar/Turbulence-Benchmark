
def find_second_smallest_num(num_list):
    try:
        segment = num_list[29:52]
        segment.sort()
        return segment[1]
    except:
        return None
