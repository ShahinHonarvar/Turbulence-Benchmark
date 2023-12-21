
def find_second_largest_num(numbers_list):
    try:
        filtered_list = numbers_list[59:98]
        filtered_list.sort()
        return filtered_list[-2]
    except IndexError:
        return None
