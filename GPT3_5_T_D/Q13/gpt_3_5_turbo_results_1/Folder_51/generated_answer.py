
def find_second_largest_num(numbers):
    numbers = numbers[1:9] if len(numbers) > 8 else numbers
    numbers.sort()
    return numbers[-2] if len(numbers) > 1 else None
