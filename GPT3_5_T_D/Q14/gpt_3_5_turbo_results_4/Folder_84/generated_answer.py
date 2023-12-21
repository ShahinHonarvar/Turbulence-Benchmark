
def find_second_smallest_num(numbers):
    numbers = sorted(numbers[40:81])
    if len(numbers) < 2:
        return None
    return numbers[1]
