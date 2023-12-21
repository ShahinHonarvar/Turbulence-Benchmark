
def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    numbers = numbers[34:56]
    numbers = sorted(numbers, reverse=True)
    return numbers[1]
