
def find_second_smallest_num(numbers):
    numbers = numbers[28:39]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]
