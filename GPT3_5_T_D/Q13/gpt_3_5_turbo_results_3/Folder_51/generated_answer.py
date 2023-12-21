
def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1] if len(numbers) > 1 else None
