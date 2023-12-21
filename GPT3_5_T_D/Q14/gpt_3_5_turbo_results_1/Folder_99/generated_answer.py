
def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    numbers = numbers[608:610]
    numbers.sort()
    return numbers[1]
