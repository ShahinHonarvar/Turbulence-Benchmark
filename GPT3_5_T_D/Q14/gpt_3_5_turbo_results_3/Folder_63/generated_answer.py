
def find_second_smallest_num(numbers):
    numbers = numbers[56:83]
    numbers.sort()
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]
