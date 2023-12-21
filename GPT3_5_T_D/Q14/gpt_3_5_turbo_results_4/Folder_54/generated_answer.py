
def find_second_smallest_num(numbers):
    numbers = sorted(numbers[68:87])
    if len(numbers) < 2:
        return None
    return numbers[1]
