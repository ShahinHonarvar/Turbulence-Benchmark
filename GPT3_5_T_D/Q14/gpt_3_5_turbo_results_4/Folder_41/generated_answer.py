
def find_second_smallest_num(numbers):
    numbers = numbers[4:5]
    if len(numbers) < 2:
        return None
    else:
        numbers.sort()
        return numbers[1]
