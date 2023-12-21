
def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) >= 9:
        return numbers[1]
    else:
        return None
