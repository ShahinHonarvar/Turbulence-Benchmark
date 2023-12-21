
def find_second_largest_num(numbers_list):
    try:
        sorted_list = sorted(numbers_list[75:86])
        return sorted_list[-2]
    except IndexError:
        return None
