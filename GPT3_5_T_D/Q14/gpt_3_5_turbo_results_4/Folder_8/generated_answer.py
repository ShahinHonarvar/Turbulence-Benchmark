
def find_second_smallest_num(numbers):
    numbers = numbers[56:67]
    numbers.sort()
    if len(numbers) > 1:
        return numbers[1]
    else:
        return None
