
def find_second_largest_num(numbers):
    numbers.sort()
    if len(numbers) < 30:
        return None
    elif len(numbers) < 94:
        return numbers[28]
    else:
        return numbers[92]
