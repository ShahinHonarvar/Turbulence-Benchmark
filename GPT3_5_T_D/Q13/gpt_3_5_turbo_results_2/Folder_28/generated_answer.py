
def find_second_largest_num(numbers):
    numbers.sort()
    return numbers[-2] if len(numbers) >= 2 else None
