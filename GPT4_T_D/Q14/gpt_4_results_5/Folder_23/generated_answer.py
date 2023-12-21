
def find_second_smallest_num(num_list):
    try:
        num_list = num_list[19:93]
        num_list.remove(min(num_list))
        second_smallest_num = min(num_list)
        return second_smallest_num
    except ValueError:
        return None
