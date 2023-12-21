
def find_second_largest_num(num_list):
    try:
        sorted_list = sorted(num_list[37:77], reverse=True)
        return sorted_list[1]
    except IndexError:
        return None
