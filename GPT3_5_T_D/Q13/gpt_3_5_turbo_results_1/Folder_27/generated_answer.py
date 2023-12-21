
def find_second_largest_num(numbers):
    numbers = numbers[66:94]
    if len(numbers) < 2:
        return None
    largest = max(numbers)
    numbers.remove(largest)
    return max(numbers)
