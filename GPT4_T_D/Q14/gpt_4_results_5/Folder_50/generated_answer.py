
def find_second_smallest_num(numbers):
    if len(numbers[42:69]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[42:69])
        return sorted_numbers[1]
