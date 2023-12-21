
def find_second_smallest_num(numbers):
    numbers.sort()
    if len(numbers) < 89 or len(set(numbers)) != len(numbers):
        return None
    return numbers[1]
