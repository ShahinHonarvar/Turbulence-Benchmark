
def find_second_smallest_num(numbers):
    if len(numbers) < 539:
        return None
    sorted_numbers = sorted(numbers[527:539])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]
