
def find_second_smallest_num(numbers):
    numbers = numbers[50:201]
    if len(numbers) > 1:
        numbers.sort()
        return numbers[1]
    else:
        return None
