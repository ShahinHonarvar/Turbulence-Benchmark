
def find_second_largest_num(numbers):
    sorted_list = sorted(numbers[55:99])
    if len(sorted_list) >= 2:
        return sorted_list[-2]
    else:
        return None
