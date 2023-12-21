
def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]
