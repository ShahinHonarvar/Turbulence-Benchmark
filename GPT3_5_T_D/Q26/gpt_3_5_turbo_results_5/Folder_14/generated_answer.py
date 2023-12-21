
def sum_in_range(numbers):
    return sum(num for num in numbers if 3 <= num <= 7) if any(3 <= num <= 7 for num in numbers) else 0
