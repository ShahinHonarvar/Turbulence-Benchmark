
def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    numbers = numbers[37:77]
    numbers.sort()
    if len(numbers) >= 2:
        return numbers[1]
    else:
        return None
