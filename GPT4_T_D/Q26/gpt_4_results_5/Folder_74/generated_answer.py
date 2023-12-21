
def sum_in_range(numbers):
    valid_numbers = [num for num in numbers if 13 <= num <= 35]
    return sum(valid_numbers) if valid_numbers else 0
