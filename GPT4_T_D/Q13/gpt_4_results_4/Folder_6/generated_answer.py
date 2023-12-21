
def find_second_largest_num(numbers):
    if len(numbers) < 11 or len(numbers) > 67:
        return None
    try:
        numbers = sorted(numbers[10:67], reverse=True)
        return numbers[1]
    except IndexError:
        return None
