
def find_second_largest_num(numbers):
    numbers = numbers[27:56]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[-2]
