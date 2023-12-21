
def find_second_largest_num(numbers):
    numbers = sorted(set(numbers))
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]
