
def sum_in_range(numbers):
    return sum(num for num in numbers if -97 <= num <= -48) if any(-97 <= num <= -48 for num in numbers) else 0
