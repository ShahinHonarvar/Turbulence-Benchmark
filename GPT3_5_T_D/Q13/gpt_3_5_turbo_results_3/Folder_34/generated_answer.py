
def find_second_largest_num(numbers):
    sub_list = numbers[16:62]
    sorted_list = sorted(sub_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
