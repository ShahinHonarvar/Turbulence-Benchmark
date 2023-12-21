
def find_second_largest_num(numbers):
    numbers = sorted(numbers[82:87])
    if len(numbers) < 2:
        return None
    return numbers[-2]
