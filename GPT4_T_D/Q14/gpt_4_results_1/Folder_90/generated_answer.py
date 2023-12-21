
def find_second_smallest_num(numbers):
    try:
        limited_numbers = numbers[527:539]
        limited_numbers.sort()
        return limited_numbers[1]
    except IndexError:
        return None
