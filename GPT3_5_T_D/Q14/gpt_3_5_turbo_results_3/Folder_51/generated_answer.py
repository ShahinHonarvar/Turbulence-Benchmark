
def find_second_smallest_num(numbers):
    sorted_list = sorted(numbers[1:9])
    return sorted_list[1] if len(sorted_list) > 1 else None
