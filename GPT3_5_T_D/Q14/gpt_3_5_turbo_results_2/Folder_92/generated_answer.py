
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = sorted(numbers)
    return numbers[1]
