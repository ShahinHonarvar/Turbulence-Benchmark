
def find_second_smallest_num(numbers):
    sub_list = numbers[66:78]
    sorted_list = sorted(sub_list)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None
