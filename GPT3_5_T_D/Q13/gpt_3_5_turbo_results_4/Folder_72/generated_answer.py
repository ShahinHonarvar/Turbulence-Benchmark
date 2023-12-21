
def find_second_largest_num(numbers):
    numbers = sorted(numbers[29:52])
    if len(numbers) >= 2:
        return numbers[-2]
    else:
        return None
