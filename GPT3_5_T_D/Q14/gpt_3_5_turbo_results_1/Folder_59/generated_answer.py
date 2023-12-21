
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(set(numbers))
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    return None
