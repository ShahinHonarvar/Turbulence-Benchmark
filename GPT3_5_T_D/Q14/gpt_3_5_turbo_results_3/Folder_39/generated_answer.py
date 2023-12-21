
def find_second_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    numbers = numbers[28:41]
    numbers.sort()
    if len(numbers) <= 1:
        return None
    return numbers[1]
