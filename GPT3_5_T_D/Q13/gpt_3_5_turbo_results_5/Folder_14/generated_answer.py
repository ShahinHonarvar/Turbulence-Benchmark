
def find_second_largest_num(numbers):
    numbers = numbers[5:8]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[-2]
