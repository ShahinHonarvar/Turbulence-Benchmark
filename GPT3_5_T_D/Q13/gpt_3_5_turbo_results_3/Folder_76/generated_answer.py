
def find_second_largest_num(numbers):
    sub_list = numbers[686:988]
    sorted_list = sorted(sub_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
