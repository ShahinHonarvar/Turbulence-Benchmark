
def find_second_smallest_num(numbers):
    numbers = numbers[13:69]
    numbers.sort()
    if len(numbers) <= 1:
        return None
    return numbers[1]
