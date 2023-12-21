
def find_second_smallest_num(numbers):
    try:
        numbers = numbers[37:52]
        numbers.sort()
        return numbers[1]
    except IndexError:
        return None
