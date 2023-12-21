
def find_second_smallest_num(numbers):
    return sorted(numbers[55:98])[1] if len(sorted(numbers[55:98])) > 1 else None
