
def find_second_smallest_num(numbers):
    numbers = numbers[62:100]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]
