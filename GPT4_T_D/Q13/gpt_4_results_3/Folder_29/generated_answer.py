
def find_second_largest_num(numbers_list):
    sliced_list = numbers_list[59:98]
    if not sliced_list:
        return None
    sliced_list.sort()
    return sliced_list[-2] if len(sliced_list) > 1 else None
