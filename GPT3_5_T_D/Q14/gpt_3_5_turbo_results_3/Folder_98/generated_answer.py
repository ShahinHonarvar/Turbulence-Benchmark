
def find_second_smallest_num(numbers):
    numbers = sorted(numbers[6:7])
    if len(numbers) >= 2:
        return numbers[1]
    else:
        return None
