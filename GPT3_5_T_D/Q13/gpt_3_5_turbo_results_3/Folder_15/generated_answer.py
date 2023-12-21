
def find_second_largest_num(numbers):
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[-2] if len(numbers) >= 2 else None
