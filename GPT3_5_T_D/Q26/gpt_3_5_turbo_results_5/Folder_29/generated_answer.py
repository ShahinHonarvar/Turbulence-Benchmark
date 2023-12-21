
def sum_in_range(numbers):
    return sum(i for i in numbers if 18 <= i <= 60) if any(18 <= i <= 60 for i in numbers) else 0
