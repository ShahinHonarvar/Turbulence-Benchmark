
def find_second_largest_num(numbers):
    numbers = numbers[13:69]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[-2]
