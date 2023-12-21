
def find_second_largest_num(numbers):
    numbers = sorted(numbers, reverse=True)
    if len(numbers) <= 1:
        return None
    return numbers[1]
