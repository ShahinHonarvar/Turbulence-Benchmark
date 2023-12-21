
def find_second_smallest_num(numbers):
    sorted_list = sorted(numbers[25:60])
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None
