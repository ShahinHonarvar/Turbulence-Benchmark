
def find_second_smallest_num(num_list):
    try:
        sorted_list = sorted(num_list[66:78])
        return sorted_list[1]
    except IndexError:
        return None
