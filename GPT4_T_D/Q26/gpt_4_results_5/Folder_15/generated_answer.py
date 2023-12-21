
def sum_in_range(numbers):
    valid_numbers = [num for num in numbers if 6 <= num <= 9]
    return sum(valid_numbers) if valid_numbers else 0
