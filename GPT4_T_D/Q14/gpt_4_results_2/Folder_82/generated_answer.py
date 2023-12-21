
def find_second_smallest_num(numbers):
    if len(numbers) < 22 or len(numbers) > 201:
        return None
    subset_numbers = numbers[20:201]
    subset_numbers.sort()
    return subset_numbers[1] if len(subset_numbers) >= 2 else None
