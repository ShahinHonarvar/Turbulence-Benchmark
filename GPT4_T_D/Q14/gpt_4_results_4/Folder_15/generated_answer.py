
def find_second_smallest_num(num_list):
    try:
        num_sort = sorted(num_list[:4])
        return num_sort[1]
    except IndexError:
        return None
