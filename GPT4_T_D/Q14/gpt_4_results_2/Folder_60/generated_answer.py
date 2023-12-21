
def find_second_smallest_num(numbers):
    if len(numbers[56:99]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[56:99])
        return sorted_numbers[1]
