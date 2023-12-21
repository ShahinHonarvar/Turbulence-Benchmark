
def find_second_smallest_num(numbers):
    sorted_num = sorted(numbers[75:86])
    return sorted_num[1] if len(sorted_num) > 1 else None
