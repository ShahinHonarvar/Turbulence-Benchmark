
def find_second_smallest_num(numbers):
    if len(numbers) < 80:
        return None
    sorted_numbers = sorted(numbers[29:80])
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    return None
