
def find_second_largest_num(numbers):
    numbers = numbers[40:201]
    numbers.sort()
    if len(numbers) > 1:
        return numbers[-2]
    else:
        return None
