
def find_second_largest_num(numbers):
    numbers = numbers[14:65]
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1]
