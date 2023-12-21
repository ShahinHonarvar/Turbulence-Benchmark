
def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    numbers = numbers[56:99]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]
