
def find_second_smallest_num(numbers):
    numbers = numbers[23:24]
    if len(numbers) == 0:
        return None
    numbers.sort()
    return numbers[0]
