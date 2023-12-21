
def find_second_largest_num(numbers):
    numbers = numbers[1:6]
    numbers.sort()
    if len(numbers) > 1:
        return numbers[-2]
    else:
        return None
