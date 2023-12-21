
def find_second_smallest_num(num_list):
    try:
        return sorted(num_list[80:201])[1]
    except IndexError:
        return None
