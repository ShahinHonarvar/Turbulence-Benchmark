
def sum_in_range(numbers):
    numbers_in_range = [num for num in numbers if 273 <= num <= 451]
    return sum(numbers_in_range) if numbers_in_range else 0
