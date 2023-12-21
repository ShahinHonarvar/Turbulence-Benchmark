
def find_second_largest_num(numbers):
    numbers = numbers[310:371]
    numbers.sort()
    if len(numbers) < 2:
        return None
    else:
        return numbers[-2]
