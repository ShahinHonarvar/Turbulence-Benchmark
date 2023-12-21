
def find_second_smallest_num(numbers):
    numbers = sorted(numbers[37:52])
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]
