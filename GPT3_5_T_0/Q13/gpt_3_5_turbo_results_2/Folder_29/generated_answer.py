
def find_second_largest_num(numbers):
    if len(numbers) < 98:
        return None
    numbers = numbers[59:98]
    numbers.sort()
    return numbers[-2] if len(numbers) >= 2 else None
