
def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    numbers = numbers[4:9]
    numbers.sort(reverse=True)
    return numbers[1]
