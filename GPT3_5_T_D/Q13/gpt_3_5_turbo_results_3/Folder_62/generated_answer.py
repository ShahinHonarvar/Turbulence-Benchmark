
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[91:100])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[-2]
