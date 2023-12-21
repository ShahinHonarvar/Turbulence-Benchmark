
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1]
