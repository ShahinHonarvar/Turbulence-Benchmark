
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1] if len(numbers) >= 8 else None
