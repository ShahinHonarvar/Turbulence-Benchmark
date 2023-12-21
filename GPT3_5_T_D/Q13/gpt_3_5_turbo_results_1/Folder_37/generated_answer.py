
def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) < 2 or len(numbers) <= 5:
        return None
    return numbers[1]
