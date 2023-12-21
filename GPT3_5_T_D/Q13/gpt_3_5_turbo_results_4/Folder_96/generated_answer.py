
def find_second_largest_num(numbers):
    sub_list = numbers[15:52]
    sorted_list = sorted(sub_list, reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None
