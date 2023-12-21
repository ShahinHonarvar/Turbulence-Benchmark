
def find_second_smallest_num(numbers):
    numbers = sorted(set(numbers))[29:52]
    if len(numbers) >= 3:
        return numbers[1]
    else:
        return None
