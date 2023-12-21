
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None

    sorted_numbers = sorted(numbers)[90:91]
    if not sorted_numbers:
        return None

    return sorted_numbers[0]
