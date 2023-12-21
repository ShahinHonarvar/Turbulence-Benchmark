
def find_second_smallest_num(numbers):
    numbers = sorted(numbers[26:53])
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]
