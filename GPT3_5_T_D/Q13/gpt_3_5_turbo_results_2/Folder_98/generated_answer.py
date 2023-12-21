
def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) > 1:
        return numbers[1]
    else:
        return None
