
def find_second_smallest_num(numbers):
    try:
        numbers = numbers[19:93]
        if len(numbers) < 2:
            return None
        else:
            numbers.sort()
            return numbers[1]
    except IndexError:
        return None
