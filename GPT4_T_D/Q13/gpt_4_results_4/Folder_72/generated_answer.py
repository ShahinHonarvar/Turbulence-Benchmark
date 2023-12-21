
def find_second_largest_num(numbers):
    numbers = numbers[29:52]
    if not numbers:
        return None
    else:
        numbers.sort()
        return numbers[-2] if len(numbers) > 1 else None
