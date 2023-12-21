
def find_second_largest_num(numbers):
    try:
        numbers_35_to_49 = numbers[35:50]
        numbers_35_to_49.sort()
        return numbers_35_to_49[-2]
    except IndexError:
        return None
