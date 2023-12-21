
def find_second_largest_num(numbers_list):
    if len(numbers_list[59:98])<2:
        return None
    else:
        sorted_list = sorted(numbers_list[59:98])
        return sorted_list[-2]
