
def find_second_smallest_num(numbers):
    numbers = numbers[25:60]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]
