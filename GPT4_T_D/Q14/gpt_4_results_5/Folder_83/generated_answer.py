
def find_second_smallest_num(num_list):
    try:
        sliced_list = num_list[90:201]
        sliced_list.sort()
        return sliced_list[1]
    except IndexError:
        return None
