
def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    numbers = numbers[30:49]
    numbers.sort()
    return numbers[1]
